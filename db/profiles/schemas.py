from typing import Any

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class ProfileModel(BaseModel):
    id: int = None
    user_id: int = None
    username: str = None
    is_bot: bool = None
    first_name: str = None
    lang_code: str = None
    is_banned: bool = None
    count_of_ban: int = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class AccessTokenModel(BaseModel):
    access_token: str = None
    token_type: str = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserLogin(ProfileModel):
    username: str = None
    one_time_code: int | str = None


class TokenData(BaseModel):
    user_id: str = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class TestUserSchema(BaseModel):
    port: str = None
