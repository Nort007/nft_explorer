from .base_schema import BaseConfigModel


class UserIsActive(BaseConfigModel):
    is_active: bool = False


class UserModel(BaseConfigModel):
    id: int = None
    user_id: int = None
    username: str = None
    is_bot: bool = False
    first_name: str = None
    lang_code: str = None
    is_banned: bool = False
    count_of_ban: int = None


# class AccessTokenModel(BaseConfigModel):
#     access_token: str = None
#     token_type: str = None


class UserLogin(BaseConfigModel):
    username: str = None
    one_time_code: int | str = None
