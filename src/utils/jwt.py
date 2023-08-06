from datetime import datetime, timedelta, timezone

import jwt

from src.config.const import SECRET_KEY


def generate_jwt_token(user_id: int) -> str:
    return jwt.encode(
        {
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=1),
            "user_id": user_id,
        },
        SECRET_KEY,
        algorithm="HS256",
    )


def decode_jwt_token(token: str) -> int:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload["user_id"]
