from misc import on_startup, dp
from aiogram import executor

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup(), skip_updates=True)
