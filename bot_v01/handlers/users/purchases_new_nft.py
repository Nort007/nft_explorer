from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram import types
from bot_v01.keyboards.inline.menu import watchlist_menu
from aiogram.dispatcher.filters.state import State, StatesGroup


class NFTState(StatesGroup):
    name_or_address = State()


async def new_nft_to_watchlist(q: types.Message):
    """Обработчик команды /newnft.
    Добавляет новый нфт в базу данных watchlist
    и далее привязывает автоматически к юзеру
    в conditions с дефолтными значениями"""
    await q.answer("Insert NFT name or address")
    await NFTState.name_or_address.set()


async def valid_data(q: types.Message, state: FSMContext):
    """Проверяет валидность данных путем обработки через запрос по апи и возвращение результата"""
    # await call.answer(cache_time=10)
