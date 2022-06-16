"""Basic module for JWT and refresh JWT."""
import time
from datetime import datetime, timedelta

import jwt

from core.config import SECRET_KEY, TTL_TRIGGER

ALGORITHM = 'HS256'
access_token_jwt_subject = 'access'


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=1)
    to_encode.update({'exp': expire, 'sub': access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def refresh_jwt_token(**kw):
    payload = kw.get('payload', {})
    if (payload['exp'] - int(time.time())) < TTL_TRIGGER:
        return create_access_token(
            data={'user_id': payload['user_id'], 'username': payload['username']}, expires_delta=timedelta(seconds=kw.get('ttl_refresh', 120))
        )
    else:
        pass
