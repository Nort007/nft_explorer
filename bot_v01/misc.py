import logging
import os

import coloredlogs
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from core.config import TELEGRAM_TOKEN

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', fmt='%(asctime)s: %(levelname)s: [%(funcName)s: %(filename)s: %(module)s:] %(message)s')
bot = Bot(token=TELEGRAM_TOKEN)
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
