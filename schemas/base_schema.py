from typing import Any

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict

from api.services.camel_case import to_camel_case


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class BaseConfigModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        alias_generator = to_camel_case
        allow_population_by_field_name = True
