import os
from pathlib import Path

from dotenv import load_dotenv

env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)

PG_DATABASE_NAME = os.getenv('PG_DB')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASS')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_IP = os.getenv('REDIS_IP')
TELEGRAM_API = os.getenv('TELEGRAM_API')
TELEGRAM_TOKEN = os.getenv('TG_TOKEN')
SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8
TTL_SECONDS = 60
TTL_REFRESH = 900
TTL_TRIGGER = 300
TOKEN_TYPE = 'bearer'
