from fastapi import APIRouter

from api.endpoints.authentication import login
from api.endpoints.user import user

route = APIRouter()
route.include_router(login.router, tags=["authentication"], prefix="/v1")
route.include_router(user.router, tags=["client"], prefix="/v1")
