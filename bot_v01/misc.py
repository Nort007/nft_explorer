import os
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
import logging
from aiogram.contrib.fsm_storage.redis import RedisStorage2


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s - func: [%(funcName)s] - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)
env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)
TG_TOKEN = os.getenv('TG_TOKEN')
bot = Bot(token=TG_TOKEN)
storage = RedisStorage2(host='localhost', port=6379, password='WERKGPqoRTk7D', state_ttl=120, bucket_ttl=500, data_ttl=120)
dp = Dispatcher(bot, storage=storage)


def on_startup():
    import middlewares
    import handlers

    middlewares.setup(dp)
    handlers.base.setup(dp)
    handlers.users.setup_purchases_new_nft(dp)
    handlers.users.setup(dp)
