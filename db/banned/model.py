from datetime import datetime
from peewee import DateTimeField, ForeignKeyField
from db.base.base_model import BaseModel
from db.profiles.model import ProfileModel


class BanModel(BaseModel):
    expiration: datetime = DateTimeField(null=datetime.now)
    profile_id = ForeignKeyField(ProfileModel, backref='bans')

    class Meta:
        db_table = 'banned'
