from aiogram import types
from bot_v01.keyboards.inline.menu import watchlist_menu


async def watchlist_command(q: types.Message | types.CallbackQuery):
    """Обработчик команды /mywatchlist, либо если выбран инлайн,
     '<< Back' То возвращается в главное меню с списком из нфт"""
    text_response = '🗂 User watchlist:'
    del_menu = False
    if q.text == '/delnft':
        del_menu = True
    # print(watchlist_menu(q.from_user.id, del_menu=del_menu))
    if isinstance(q, types.Message):
        await q.answer(text_response, reply_markup=watchlist_menu(q.from_user.id, del_menu=del_menu))
    else:
        await q.message.edit_text(text_response, reply_markup=watchlist_menu(q.from_user.id, del_menu=del_menu))
