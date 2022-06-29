from .base_schema import BaseConfigModel


class UserModel(BaseConfigModel):
    id: int = None
    user_id: int = None
    username: str = None
    is_bot: bool = None
    first_name: str = None
    lang_code: str = None
    is_banned: bool = None
    count_of_ban: int = None


# class AccessTokenModel(BaseConfigModel):
#     access_token: str = None
#     token_type: str = None


class UserLogin(BaseConfigModel):
    username: str = None
    one_time_code: int | str = None
