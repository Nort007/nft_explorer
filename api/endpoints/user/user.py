"""Endpoint of user profile, logout and other some things of a personal account."""
from fastapi import Depends, Request, APIRouter

from api.api_db_utils import get_db
from api.services.service_me import get_current_user
from core.logger_config import logger
from db.profiles import schemas

router = APIRouter()


@router.get('/me', response_model=schemas.ProfileModel, dependencies=[Depends(get_db)])
def read_me(request: Request):
    user = get_current_user(request.headers, request.client.host, request.client.port)
    logger.debug('USER: %s %s', user.username, user.user_id)
    return user
