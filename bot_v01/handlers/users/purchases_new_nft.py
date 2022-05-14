from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram import types
from bot_v01.keyboards.inline.menu import new_nft_menu
from aiogram.dispatcher.filters.state import State, StatesGroup


class NFTState(StatesGroup):
    name_or_address = State()


async def new_nft_to_watchlist(q: Message):
    """Обработчик команды /newnft.
    Добавляет новый нфт в базу данных watchlist и далее привязывает автоматически к юзеру
    в conditions с дефолтными значениями"""
    await q.answer("Choose search format", reply_markup=new_nft_menu())
    print()
    # await NFTState.name_or_address.set()


async def choosen_option(q: CallbackQuery):
    """Обрабатывает нажатие и отсюда вызывается обновление пейлода по какому значению искать в апи информацию."""
    await q.answer(cache_time=10)
    data = q.data.split(':')
    if data[-1] == 'name':
        pass
    elif data[-1] == 'address':
        pass
    print(data)


async def valid_data(q: types.Message, state: FSMContext):
    """Проверяет валидность данных путем обработки через запрос по апи и возвращение результата"""
    # await call.answer(cache_time=10)
    await q.answer("Получены данные. Проверяй редис.")
    curr_data = await state.update_data(name_or_address=q.text)
