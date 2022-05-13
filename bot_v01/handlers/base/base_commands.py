from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_v01.misc import logger
from bot_v01.services.service_db import add_new_user


async def start(message: types.Message):
    """/start - команда регает юзера, основная команда для начала работы бота"""
    print(message.from_user)
    add_new_user(user_id=message.from_user.id, is_bot=message.from_user.is_bot, first_name=message.from_user.first_name, username=message.from_user.username,
                 lang_code=message.from_user.language_code)
    await message.answer('Initial start')


async def help(message: types.Message):
    """/help Показывает команды доступные, они будут вывыдены в чат бота,
    команда доступна зареганым юзерам т.к. показывает команды для зареганых юзеров."""
    await message.answer('Help')


async def cancel(message: types.Message, state: FSMContext = None):
    """/cancel - Отмменяет текущее дейсвтие состояния (в основном)"""
    curr = await state.get_state()
    if curr is None:
        logger.debug('Cancel: No state')
        await message.answer(text=f'Canceled state: {curr}')
        return
    logger.debug(f'Cancel {curr}')
    await state.finish()
    await message.answer(text='Canceled')

