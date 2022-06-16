from fastapi import FastAPI

from api.routes import route


def main() -> FastAPI:
    app = FastAPI()
    app.include_router(route, prefix="/api")
    return app


app = main()
