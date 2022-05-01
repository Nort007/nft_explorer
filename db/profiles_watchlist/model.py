from peewee import ForeignKeyField
from db.base.base_model import BaseModel
from db.profiles.model import ProfileModel
from db.watchlist.model import WatchlistModel


class ProfileWatchlistModel(BaseModel):
    profile_id: int = ForeignKeyField(WatchlistModel, backref='watchlist')
    watchlist_id: int = ForeignKeyField(ProfileModel, backref='profiles')

    class Meta:
        db_table = 'profiles_watchlist'
