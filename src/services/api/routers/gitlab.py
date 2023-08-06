import jwt
from fastapi import APIRouter, Depends, Response
from gitlab import Gitlab
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.db.models import User
from src.services.gitlab.interface import get_access_token
from src.utils.jwt import decode_jwt_token

router = APIRouter()


@router.get("/callback/")
async def gitlab_callback(
    code: str, state: str, session: AsyncSession = Depends(get_session)
):
    """
    After user authorized at gitlab application,
    that router should be called by gitlab redirection
    """
    try:
        user_id = decode_jwt_token(state)
    except jwt.ExpiredSignatureError:
        return Response("not authorized", status_code=401)
    except jwt.InvalidSignatureError:
        return Response("not authorized", status_code=401)

    access_token_response = get_access_token(code)
    gitlab = Gitlab(oauth_token=access_token_response["access_token"])
    gitlab.user
    try:
        gitlab.auth()
    except:
        return Response("not authorized", status_code=401)

    query = select(User).filter(User.telegram_id == user_id)
    result = await session.execute(query)
    user: User = result.scalar_one()

    if gitlab.user is not None and (gitlab_user_data := gitlab.user.asdict()):
        user.gitlab_profile_id = gitlab_user_data["id"]
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return {
        "user": {
            "tg_id": user.telegram_id,
            "gitlab_profile_id": user.gitlab_profile_id,
            "gitlab_oauth_token": code,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
        "gitlab_user": gitlab.user.asdict() if gitlab.user else {},
        "state": state,
        "access_token_response": access_token_response,
    }
