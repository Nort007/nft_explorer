from pydantic import BaseModel


class SuccessToken(BaseModel):
    status: bool = False
    msg: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    user_id: str
    username: str
