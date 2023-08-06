import requests
from requests import auth

from src.config.const import BACKEND_URL, GITLAB_APP_ID, GITLAB_APP_SECRET


def get_access_token(code: str) -> dict:
    client_auth = auth.HTTPBasicAuth(GITLAB_APP_ID, GITLAB_APP_SECRET)
    post_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": f"{BACKEND_URL}/api/v1/gitlab/callback",
    }
    response = requests.post(
        "https://gitlab.com/oauth/token", auth=client_auth, data=post_data
    )
    return response.json()


def refresh_access_token(code: str, refresh_token: str) -> dict:
    client_auth = auth.HTTPBasicAuth(GITLAB_APP_ID, GITLAB_APP_SECRET)
    post_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": f"{BACKEND_URL}/api/v1/gitlab/callback",
    }
    response = requests.post(
        "https://gitlab.com/oauth/token", auth=client_auth, data=post_data
    )
    return response.json()
