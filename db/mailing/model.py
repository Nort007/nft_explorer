from peewee import CharField, ForeignKeyField, BigIntegerField, BooleanField
from db.base.base_model import BaseModel
from db.profiles.model import ProfileModel


class MailingModel(BaseModel):
    public_channel: str = CharField(max_length=254)
    private_channel: int = BigIntegerField()
    active: bool = BooleanField(default=False)
    profile_id: int = ForeignKeyField(ProfileModel)

    class Meta:
        table_name = 'mailing'
