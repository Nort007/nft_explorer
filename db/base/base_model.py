from peewee import PostgresqlDatabase, Model, DateTimeField
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import os

env = Path(os.path.dirname(__file__)).parent.parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)
psql_db = PostgresqlDatabase(
    database=os.getenv('PG_DB'),
    user=os.getenv('PG_USER'),
    password=os.getenv('PG_PASS'),
    host='localhost',
    port=os.getenv('PG_PORT'))


class BaseModel(Model):
    created_at: datetime = DateTimeField(default=datetime.now)
    updated_at: datetime = DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        database = psql_db
