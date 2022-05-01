from aiogram.dispatcher.filters import CommandStart
from bot.misc import dp
from bot.utils.slash_commands import start_command


def register_common_handlers():
    dp.register_message_handler(start_command, CommandStart())

