from http import HTTPStatus

import jwt
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from gitlab import Gitlab
from gitlab.exceptions import GitlabAuthenticationError
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.db.models import User
from src.services.gitlab.auth import get_access_token
from src.utils.bot import get_bot_username
from src.utils.jwt import decode_jwt_token

router = APIRouter()


@router.get("/callback")
async def gitlab_callback(
    code: str, state: str, session: AsyncSession = Depends(get_session)
):
    """
    After user authorized at gitlab application,
    that router should be called by gitlab redirection
    after succed redirecting to telegram bot
    """
    try:
        payload = decode_jwt_token(state)
    except jwt.ExpiredSignatureError:
        # TODO: redirect to bot and send message in telegram if expired, ask user to authorize again
        raise HTTPException(
            HTTPStatus.UNAUTHORIZED,
            {"token": "expired"},
        )
    except jwt.InvalidSignatureError:
        raise HTTPException(
            HTTPStatus.UNAUTHORIZED,
            {"token": "invalid"},
        )

    access_token_response = get_access_token(code=code)
    gitlab = Gitlab(oauth_token=access_token_response["access_token"])
    try:
        gitlab.auth()
    except GitlabAuthenticationError as e:
        logger.error(e)
        # TODO: redirect to bot and send message in telegram
        raise e

    if gitlab.user is None or not (gitlab_user_data := gitlab.user.asdict()):
        raise GitlabAuthenticationError

    user = await User.get_by_pk(pk=payload["user_id"], session=session)
    if not user:
        raise HTTPException(
            HTTPStatus.NOT_FOUND,
            {"details": f"user: {payload['user_id']} not found"},
        )

    await user.save_gitlab_token(
        access_token=access_token_response["access_token"],
        refresh_token=access_token_response["refresh_token"],
        oauth_code=code,
    )

    user.gitlab_profile_id = gitlab_user_data["id"]
    user = await user.save(session=session)

    tg_bot_username = await get_bot_username()
    return RedirectResponse(
        f"https://t.me/{tg_bot_username}",
        status_code=HTTPStatus.MOVED_PERMANENTLY,
    )
