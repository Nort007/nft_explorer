from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import route


def main() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    app.include_router(route, prefix="/api")
    return app


app = main()
