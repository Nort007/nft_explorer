from .base_schema import BaseConfigModel


class SuccessToken(BaseConfigModel):
    status: bool = False
    msg: str


class Token(BaseConfigModel):
    access_token: str
    token_type: str


class TokenPayload(BaseConfigModel):
    user_id: str
    username: str
