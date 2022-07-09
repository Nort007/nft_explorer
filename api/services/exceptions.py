"""Basic exceptions."""
from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from core.logger_config import logger


def one_time_code_exception(detail: str = 'Verify code is not correct') -> HTTPException:
    logger.debug(detail)
    return HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=detail)


def user_not_found(detail: str = 'User not found') -> HTTPException:
    logger.debug(detail)
    return HTTPException(status_code=HTTP_404_NOT_FOUND, detail=detail)


def user_forbidden() -> HTTPException:
    detail = {"message": "Could not validate credentials", "status": HTTP_403_FORBIDDEN}
    return HTTPException(status_code=HTTP_403_FORBIDDEN, detail=detail)
