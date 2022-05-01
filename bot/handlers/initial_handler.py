from aiogram import types
from bot.misc import dp
from bot.utils.keyboards import initial_menu


# @dp.message_handler(lambda message: message.text == 'NFT menu')
# async def main_nft_menu(message: types.Message):
#     print(message.from_user.values)
#     await message.answer(
#         f"📎 Ok. NFT Menu.\n\n", reply_markup=nft_menu()
#     )
#
#
# @dp.message_handler(lambda message: message.text == 'Exit')
# async def exit_(message: types.Message):
#     await message.answer(
#         f"🖖 Ok. Bye.\n\n", reply_markup=types.ReplyKeyboardRemove()
#     )


@dp.message_handler(lambda message: message.text == 'Back to main menu')
async def cancel(message: types.Message):
    await message.answer(
        f"🖖 Ok. Back to main menu.\n\n", reply_markup=initial_menu()
    )
