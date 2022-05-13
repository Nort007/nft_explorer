from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Command
from .base_commands import start, help, cancel


def setup(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
    dp.register_message_handler(help, CommandHelp())
    dp.register_message_handler(cancel, Command("cancel"), state="*")
