from peewee import CharField
from db.base.base_model import BaseModel


class WatchlistModel(BaseModel):
    address: str = CharField(max_length=254)
    name: str = CharField(max_length=254)

    class Meta:
        table_name = 'watchlist'
