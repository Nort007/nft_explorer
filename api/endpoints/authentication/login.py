"""Endpoint for an initial login."""
from typing import Union

from fastapi import APIRouter, Depends, Request

from api.api_db_utils import get_db
from api.services.exceptions import user_not_found
from api.services.security import auth_user
from api.services.service_db import get_user
from core.logger_config import logger
from schemas import Token, SuccessToken, UserLogin

router = APIRouter()


@router.post('/login', response_model=Union[Token, SuccessToken], dependencies=[Depends(get_db)])
def login(user: UserLogin, request: Request):
    db_user = get_user(username=user.username)
    logger.debug('USER: %s', db_user)
    if db_user is None:
        raise user_not_found()
    user_auth = auth_user(host=request.client.host, port=request.client.port, username=db_user.username, user_id=db_user.user_id,
                          user_code=user.one_time_code)
    return user_auth
