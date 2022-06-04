import logging
import os
from pathlib import Path

import coloredlogs
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)
TG_TOKEN = os.getenv('TG_TOKEN')
bot = Bot(token=TG_TOKEN)
storage = RedisStorage2(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')), state_ttl=120, bucket_ttl=500, data_ttl=120)
dp = Dispatcher(bot, storage=storage)


def on_startup():
    import middlewares
    import handlers

    middlewares.setup(dp)
    handlers.base.setup(dp)
    handlers.users.setup_add_group_channel(dp)
    handlers.users.setup_purchases_new_nft(dp)
    handlers.users.setup(dp)
    handlers.users.setup_delnft(dp)
