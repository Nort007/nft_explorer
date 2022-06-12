from contextvars import ContextVar

import peewee

from core.config import (
    PG_DATABASE_NAME,
    PG_PASSWORD,
    PG_USER,
    PG_HOST,
    PG_PORT
)

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


# check_same_thread=False  only for SQLite
db = peewee.PostgresqlDatabase(
    database=PG_DATABASE_NAME,
    user=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT
)
db._state = PeeweeConnectionState()
