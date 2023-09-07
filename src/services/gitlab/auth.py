from typing import NoReturn

import requests
from requests import auth

from src.config.const import (
    GITLAB_APP_ID,
    GITLAB_APP_SECRET,
    GITLAB_HOST,
    GITLAB_REDIRECT_URI,
)


def get_access_token(**kwargs):
    client_auth = auth.HTTPBasicAuth(GITLAB_APP_ID, GITLAB_APP_SECRET)

    match kwargs:
        case {"code": code, **other}:
            _ = other
            data = {
                "grant_type": "authorization_code",
                "code": code,
            }
        case {"refresh_token": refresh_token}:
            data = {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
            }
        case _:
            raise TypeError(
                "should be or code, either refresh_token given to parameters"
            )

    response = requests.post(
        f"https://{GITLAB_HOST}/oauth/token",
        auth=client_auth,
        data={"redirect_uri": GITLAB_REDIRECT_URI, **data},
    )
    return response.json()
