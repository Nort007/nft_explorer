from datetime import timedelta

from api.services.one_time_code import get_one_time_code
from api.services.service_redis import hdel_from_redis, put_hset_in_redis
from core.celery_app import celery_app
from core.config import TTL_SECONDS, TOKEN_TYPE
from core.jwt import create_access_token
from core.logger_config import logger
from core.redis_app import redis_app
from .exceptions import one_time_code_exception


def auth_user(host: str, port: int, username: str, user_id: int | str, user_code: int | str = None):
    """This functionality implements the initial connection. The host serve as a key for the redis,
    and other data are stored in redis as a metadata of user.
    :param host: user ip address.
    :param port: user port.
    :param username: username. It's a unique identifier for user by telegram.
    :param user_id: user id. It's a unique identifier for user by telegram.
    :param user_code: user code. It's a unique identifier for user by telegram.
    :return: Token or SuccessToken.
    :rtype:"""
    user_info_redis = redis_app.hgetall(host)
    logger.debug('USER INFO FROM REDIS: %s', user_info_redis)
    if len(user_info_redis) == 0:
        one_time_code = get_one_time_code()
        celery_app.send_task('api.celery_worker.celery_put_in_redis',
                             args=[host, {'port': port, 'username': username, 'user_id': user_id, 'one_time_code': one_time_code}]
                             )
        celery_app.send_task('api.celery_worker.send_code', args=[username, user_id, one_time_code])
        return {
            'status': True,
            'msg': 'Check telegram'
        }
    elif len(user_info_redis) > 0:
        verify = check_verify_code(verify_code=user_code, code_from_redis=int(user_info_redis[b'one_time_code']))
        if verify:
            token = create_access_token(data={'user_id': user_id, 'username': username}, expires_delta=timedelta(seconds=TTL_SECONDS))
            activate_one_time_code(host=host, token=token)
            return {
                'access_token': token,
                'token_type': TOKEN_TYPE
            }
        else:
            raise one_time_code_exception()
    return user_info_redis


def activate_one_time_code(host: str, token: str):
    """Activate one time code and then delete it from redis and add bearer.
    :param host: user ip address.
    :param token: user token.
    :return: None."""
    put_hset_in_redis(key=host, datas={'token': token, 'activated': 1})
    hdel_from_redis(key=host, datas=['one_time_code'])


def check_verify_code(verify_code: int, code_from_redis: int | str):
    """This function implements the verification of the code.
    :param verify_code: user code.
    :param code_from_redis: code from redis.
    :return: True or False."""
    logger.debug('verify_code, code_from_redis: %s %s', verify_code, code_from_redis)
    if verify_code is not None:
        if int(verify_code) == int(code_from_redis):
            return True
    return False


def get_user_token(host: str):
    """This function implements the getting of the token from redis.
    :param host: user ip address.
    :return: token or None."""
    return redis_app.hget(host, 'token')
