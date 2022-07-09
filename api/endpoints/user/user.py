"""Endpoint of user profile, logout and other some things of a personal account."""
from fastapi import Depends, Request, APIRouter

from api.api_db_utils import get_db
from api.services.service_user import get_current_user, get_is_active
from core.logger_config import logger
from schemas import UserModel, UserIsActive

router = APIRouter()


@router.get('/user', response_model=UserModel, dependencies=[Depends(get_db)])
def user_information(request: Request):
    """Bla bla bla"""
    user = get_current_user(dict(request.headers), request.client.host, request.client.port)
    logger.debug('USER: %s %s', user.username, user.user_id)
    return user


@router.get('/is-active', response_model=UserIsActive, dependencies=[Depends(get_db)])
def is_active(request: Request):
    user_is_active = get_is_active(request.client.host)
    return user_is_active
