"""Basic exceptions."""
from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from core.logger_config import logger


def one_time_code_exception(detail: str = 'Verify code is not correct') -> HTTPException:
    logger.debug(detail)
    return HTTPException(status_code=400, detail=detail)


def user_not_found(detail: str = 'User not found') -> HTTPException:
    logger.debug(detail)
    return HTTPException(status_code=404, detail=detail)


def user_forbidden(detail: str = 'Could not validate credentials'):
    logger.debug(detail)
    return HTTPException(status_code=HTTP_403_FORBIDDEN, detail=detail)
