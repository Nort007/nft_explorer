from aiogram.types import CallbackQuery

from bot_v01.services import del_from_profiles_watchlist


async def del_user_nft(call: CallbackQuery):
    await call.answer(cache_time=10)
    call_data = call.data.split(':')
    # print(call_data, 'dsds')
    if call_data[0] == 'del':
        nft_name = call_data[1].replace('_', ' ')
        del_from_profiles_watchlist(user_id=call.from_user.id, wl_pk_id=int(call_data[2]))
        await call.message.edit_text(text=f"{nft_name} has been deleted.")
