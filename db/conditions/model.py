from peewee import ForeignKeyField, FloatField
from db.base.base_model import BaseModel
from db.profiles.model import ProfileModel
from db.watchlist.model import WatchlistModel


class ConditionModel(BaseModel):
    """Model of conditions
    qt - it's your choosen price that above of the current price
    qe - it's your choosen price that above or equal of the current price
    lt - it's your choosen price that below of the current price
    le - it's your choosen price that below or equal of the current price
    eq - it's your choosen price that equal of the current price
    If default value is -1 it's denote that the condition is not set
    """
    profile_id = ForeignKeyField(ProfileModel)
    watchlist_id = ForeignKeyField(WatchlistModel)
    gt = FloatField(null=True)
    ge = FloatField(null=True)
    lt = FloatField(null=True)
    le = FloatField(null=True)
    eq = FloatField(null=True)

    class Meta:
        db_table = 'conditions'
