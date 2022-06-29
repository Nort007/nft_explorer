"""This module contains some functions of the user profile."""
import jwt

from api.services.exceptions import user_forbidden, user_not_found
from api.services.service_db import get_user
from api.services.service_redis import put_hset_in_redis
from core.config import JWT_SECRET_KEY, TTL_REFRESH, JWT_ALGORITHM
from core.jwt import refresh_jwt_token
from schemas import TokenPayload
from .security import get_user_token


def get_current_user(user_headers: dict, host: str, port: int):
    """This function gets current user."""
    if 'authorization' in user_headers.keys():
        token = user_headers['authorization'].split(' ')[1]
    else:
        token = get_user_token(host)
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise user_forbidden()
    user = get_user(user_id=int(token_data.user_id))
    if not user:
        raise user_not_found()
    refresh_token = refresh_jwt_token(host=host, port=port, payload=payload, ttl_refresh=TTL_REFRESH)
    if refresh_token is not None:
        put_hset_in_redis(key=host, datas={'token': refresh_token}, expire=TTL_REFRESH)
    return user
