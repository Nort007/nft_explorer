from aiogram.types import CallbackQuery, Message
from bot_v01.services.service_db import get_information_of_selected_nft, update_selected_condition
from bot_v01.keyboards.inline.settings_menu import main_settings_menu
from bot_v01.keyboards.inline.settings_menu import edit_conditions_menu
from bot_v01.services.service_purchases import condition_data, get_nft_name
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bot_v01.misc import logger


class ConditionState(StatesGroup):
    name: str = State()
    watchlist_pk: int = State()
    user_pk: int = State()
    condition: str = State()
    value_of_condition: float = State()


async def selected_nft(call: CallbackQuery, state: FSMContext):
    """Выбирается конкретный объект из списка и этот метод отдает детальную информацию
    из базы данных по данной нфт для конкретного юзера если она за ним привязана"""
    await call.answer(cache_time=10)
    nft_name = get_nft_name(call.values, call.data)
    nft_info = get_information_of_selected_nft(nft_name['original'].lower()).get()
    output_text = f"Here it is {nft_info.name}\n" \
                  f"Address: {nft_info.address}\n" \
                  f"What do you want to do with the {nft_info.name}?"
    logger.debug(f'Callback data: user_id: {call.from_user.id} , call.data of inline button: {call.data}')
    await call.message.edit_text(text=output_text, reply_markup=main_settings_menu(nft_name=nft_info.id))
    print('>>>>>>>>>>>>>>>>.', nft_info.id)
    await state.update_data(name=nft_name['from_callback'], watchlist_pk=nft_info.id)


async def edit_selected_nft(call: CallbackQuery, state: FSMContext):
    """Возвращает доступные условия для изменений"""
    await call.answer(cache_time=10)
    await state.reset_state(with_data=False)
    info_list = call.data.split(':')
    watchlist_pk = info_list[-1].replace('_', ' ')
    condition_information = condition_data(user_id=call.from_user.id, wl_pk_id=int(watchlist_pk))
    list_of_conditions = [condition_information['gt'], condition_information['ge'], condition_information['lt'], condition_information['le'],
                          condition_information['eq']]
    logger.debug(f'Callback data (edit_selected_nft): user_id: {call.from_user.id} , call.data of inline button: {call.data}')
    description = f"Selected NFT: {watchlist_pk}\n" \
                  f"gt: your price > current price: {condition_information['gt']}\n" \
                  f"ge: your price >= current price: {condition_information['ge']}\n" \
                  f"lt: your price < current price: {condition_information['lt']}\n" \
                  f"le: your price <= current price: {condition_information['le']}\n" \
                  f"eq: your price = current price: {condition_information['eq']}\n"
    await state.update_data(user_pk=condition_information['profile_id'])
    await call.message.edit_text(text=description, reply_markup=edit_conditions_menu(nft_name=watchlist_pk, conditions=list_of_conditions))


async def edit_selected_conditions(call: CallbackQuery, state: FSMContext):
    """Принимает изменения по выбранному условию"""
    await call.answer(cache_time=10)
    cb_data = call.data.split(':')
    selected_condition = cb_data[1]
    await state.update_data(condition=selected_condition)
    logger.debug(f"Selected Condition: {selected_condition}")
    await call.message.answer(text='Okey, send me a new condition.')
    await ConditionState.value_of_condition.set()


async def check_valid_condition(message: Message, state: FSMContext, numb_of_failed_attempts: int = -3):
    """Проверяет валидность введеных данных если введенное является числом,
    также в качестве неудачных попыток реализовано состояние счетчика для юзера,
    """
    try:
        if isinstance(float(message.text), float):
            if float(message.text) > 0.0:
                logger.debug(f'Value is correct {message.text}')
                await state.update_data(value_of_condition=float(message.text))
                data_of_states = await state.get_data()
                print(data_of_states)
                update_selected_condition(user_pk=data_of_states['user_pk'], nft_pk=data_of_states['watchlist_pk'], condition=data_of_states['condition'],
                                          value=data_of_states['value_of_condition'])
                await state.finish()
    except ValueError as e:
        logger.debug(f'Value is not correct: {message.text}; error: {e}')
        data_of_states = await state.get_data()
        if 'value_of_condition' in data_of_states:
            await state.update_data(value_of_condition=data_of_states['value_of_condition'] - 1)
            if data_of_states['value_of_condition'] <= numb_of_failed_attempts:
                await message.answer(text='ТЕРПЕНИЯ НОЛЬ ЭБАТЬ. АТМЕНА')
                await state.reset_state()
                return
        else:
            await state.update_data(value_of_condition=-1)
        await message.reply(text='Value is not correct. Try again.')
