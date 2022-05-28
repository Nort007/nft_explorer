from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram import types
from bot_v01.keyboards.inline.menu import new_nft_menu
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_v01.services.service_prepare_text import prepare_text_to_choose_option
from bot_v01.services import bind_nft_to_user


class NFTState(StatesGroup):
    option = State()
    name_or_address = State()


async def search_option(q: Message):
    """First handler of command if user sended /newnft"""
    await q.answer("Choose search format", reply_markup=new_nft_menu())


async def choosen_option(q: CallbackQuery, state: FSMContext):
    """Takes the option from the pressing of user and put them in redis and also set the state(FSM)"""
    await q.answer(cache_time=10)
    data = q.data.split(':')
    print(data)
    await state.update_data(option=data[-1])
    text = prepare_text_to_choose_option(data[-1])
    await q.message.answer(text=text)
    await NFTState.name_or_address.set()


async def new_nft_to_watchlist(q: types.Message, state: FSMContext):
    """Добавит новую коллекцию юзеру в ватчлист, если коллекция присутствует у юзера в отслеживаемых, то выдаст сообщение об этом"""
    # await call.answer(cache_time=10)
    await q.answer("Получены данные. Проверяй редис.")
    await state.update_data(name_or_address=q.text)
    curr_data = await state.get_data()
    print(curr_data)
    bind_response = bind_nft_to_user(curr_data, user_id=q.from_user.id)
    await q.answer(bind_response['text'])
    # t = information_about_query_of_user(option=curr_data['choose'], value=curr_data['name_or_address'])
    # print(json.dumps(t['data']['collections'][0], indent=4, default=str))
    await state.finish()
