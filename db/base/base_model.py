from datetime import datetime

from peewee import Model, DateTimeField

from .database import db as psql_db


class BaseModel(Model):
    created_at: datetime = DateTimeField(default=datetime.now)
    updated_at: datetime = DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        database = psql_db
