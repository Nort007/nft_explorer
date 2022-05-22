from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram import types
from bot_v01.keyboards.inline.menu import new_nft_menu
from aiogram.dispatcher.filters.state import State, StatesGroup
# from bot_v01.services.service import information_about_query_of_user
from bot_v01.services.service_prepare_text import prepare_text_to_choose_option
import json


class NFTState(StatesGroup):
    choose = State()
    name_or_address = State()


async def new_nft_to_watchlist(q: Message):
    """First handler of command if user sended /newnft"""
    await q.answer("Choose search format", reply_markup=new_nft_menu())


async def choosen_option(q: CallbackQuery, state: FSMContext):
    """Takes the option from the pressing of user and put them in redis and also set the state(FSM)"""
    await q.answer(cache_time=10)
    data = q.data.split(':')
    await state.update_data(choose=data[-1])
    text = prepare_text_to_choose_option(data[-1])
    await q.message.answer(text=text)
    await NFTState.name_or_address.set()


async def text_data_state(q: types.Message, state: FSMContext):
    """Проверяет валидность данных путем обработки через запрос по апи и возвращение результата"""
    # await call.answer(cache_time=10)
    await q.answer("Получены данные. Проверяй редис.")
    await state.update_data(name_or_address=q.text)
    curr_data = await state.get_data()
    print(curr_data)
    # t = information_about_query_of_user(option=curr_data['choose'], value=curr_data['name_or_address'])
    # print(json.dumps(t['data']['collections'][0], indent=4, default=str))
    # await state.finish()
