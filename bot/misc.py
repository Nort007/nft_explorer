import os
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging


logging.basicConfig(level=logging.INFO)
env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)
TG_TOKEN = os.getenv('TG_TOKEN')
bot = Bot(token=TG_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())