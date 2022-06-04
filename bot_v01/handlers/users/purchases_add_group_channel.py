from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message

from bot_v01.services import prepare_channel_or_group


class GrouChannelState(StatesGroup):
    group_or_channel = State()


async def user_channel_group(message: Message):
    # await call.answer(cache_time=10)
    await message.answer(text='Введите название группы или канала')
    await GrouChannelState.group_or_channel.set()


async def user_channel_group_handler(message: Message, state: FSMContext):
    # await message.answer(cache_time=10)
    await state.update_data(group_or_channel=message.text)
    curr_data = await state.get_data()
    add_mailing = prepare_channel_or_group(curr_data['group_or_channel'], message.from_user.id)
    await state.finish()
