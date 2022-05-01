from peewee import CharField, BooleanField, IntegerField
from db.base.base_model import BaseModel


class ProfileModel(BaseModel):
    user_id: int = IntegerField(unique=True)
    is_bot: bool = BooleanField(default=False)
    first_name: str = CharField(null=False)
    username: str = CharField(null=False)
    lang_code: str = CharField(null=False)

    class Meta:
        table_name = 'profiles'