from typing import Literal, NoReturn, TypedDict, overload

class AuthenticationResponse(TypedDict):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    refresh_token: str
    scope: Literal["api"]
    created_at: int

@overload
def get_access_token(
    *, code: str | None = None, refresh_token: str | None = None
) -> AuthenticationResponse: ...
@overload
def get_access_token(*args, **kwargs) -> NoReturn: ...
