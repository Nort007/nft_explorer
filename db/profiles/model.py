from peewee import CharField, BooleanField
from db.base.base_model import BaseModel


class Profile(BaseModel):
    is_bot: bool = BooleanField(default=False)
    first_name: str = CharField(null=False)
    username: str = CharField(null=False)
    lang_code: str = CharField(null=False)

    class Meta:
        table_name = 'profiles'
