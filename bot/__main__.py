from aiogram import executor
from bot.misc import dp
import handlers


if __name__ == '__main__':
    handlers.slash_handlers.register_common_handlers()
    executor.start_polling(dp, skip_updates=True)
