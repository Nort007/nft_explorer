from peewee import CharField
from db.base.base_model import BaseModel


class WatchlistModel(BaseModel):
    address: str = CharField(max_length=254, null=True, unique=True)
    name: str = CharField(max_length=254, null=True)
    slug: str = CharField(max_length=254, null=True, unique=True)

    class Meta:
        table_name = 'watchlist'
