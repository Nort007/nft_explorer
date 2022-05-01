from aiogram import types
from bot.misc import dp
from bot.utils.keyboards import nft_menu, test1
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class AddressState(StatesGroup):
    address = State()
    # name = State()


@dp.message_handler(lambda message: message.text == 'NFT menu')
async def main_nft_menu(message: types.Message):
    print(message.from_user.values)
    await message.answer(
        f"📎 Ok. NFT Menu.\n\n", reply_markup=nft_menu()
    )


@dp.message_handler(lambda message: message.text == 'Exit')
async def exit_(message: types.Message):
    await message.answer(
        f"🖖 Ok. Bye.\n\n", reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(lambda message: message.text == 'New')
async def new_(message: types.Message):
    print(message.from_user.values)
    await message.answer(
        f"📎 Ok. Send me new address or name.\n\n", reply_markup=types.ReplyKeyboardRemove()
    )
    await AddressState.address.set()


@dp.message_handler(state=AddressState.address)
async def address_(message: types.Message, state: FSMContext):
    print(message.from_user.values)
    async with state.proxy() as data:
        data['address'] = message.text
        print(data)

    await message.answer(
        f"📎 Ok. Address is {message.text}.\n\n", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.finish()


# async def check_correct_address(message: types.Message):
#     if