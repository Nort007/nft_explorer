from aiogram.types import CallbackQuery, Message
from bot_v01.services.service_db import get_information_of_selected_nft, update_selected_condition
from bot_v01.keyboards.inline.settings_menu import main_settings_menu
from bot_v01.keyboards.inline.settings_menu import edit_conditions_menu
from bot_v01.services.prepare_data_of_conditions import condition_data
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bot_v01.misc import logger


class ConditionState(StatesGroup):
    name = State()
    condition = State()
    value_of_condition = State()


async def selected_nft(call: CallbackQuery, state: FSMContext):
    """Выбирается конкретный объект из списка и этот метод отдает детальную информацию
    из базы данных по данной нфт для конкретного юзера если она за ним привязана"""
    await call.answer(cache_time=10)
    call_data = call.data.split(':')
    nft_name = call_data[1].replace('_', ' ')
    info = get_information_of_selected_nft(nft_name)
    output_text = f"Here it is {info['name']}\n" \
                  f"Address: {info['address']}\n" \
                  f"What do you want to do with the {info['name']}?"
    logger.debug(f'Callback data: user_id: {call.from_user.id} , call.data of inline button: {call.data}')
    await call.message.edit_text(text=output_text, reply_markup=main_settings_menu(nft_name=call_data[1]))
    await state.update_data(name=nft_name)


async def edit_selected_nft(call: CallbackQuery, state: FSMContext):
    """Возвращает доступные условия для изменений"""
    await call.answer(cache_time=10)
    await state.reset_state(with_data=False)
    print(call.data)
    info_list = call.data.split(':')
    nft_name = info_list[-1].replace('_', ' ')
    condition_information = condition_data(user_id=call.from_user.id, nft_name=nft_name)
    list_of_conditions = [
        condition_information['gt'],
        condition_information['ge'],
        condition_information['lt'],
        condition_information['le'],
        condition_information['eq']
    ]
    logger.debug(f'Callback data (edit_selected_nft): user_id: {call.from_user.id} , call.data of inline button: {call.data}')
    description = f"Selected NFT: {nft_name}\n" \
                  f"gt: your price > current price: {condition_information['gt']}\n" \
                  f"ge: your price >= current price: {condition_information['ge']}\n" \
                  f"lt: your price < current price: {condition_information['lt']}\n" \
                  f"le: your price <= current price: {condition_information['le']}\n" \
                  f"eq: your price = current price: {condition_information['eq']}\n"
    await call.message.edit_text(text=description, reply_markup=edit_conditions_menu(nft_name=nft_name, conditions=list_of_conditions))


async def edit_selected_conditions(call: CallbackQuery, state: FSMContext):
    """Принимает изменения по выбранному условию"""
    print(call.data)
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
                curr_data_of_states = await state.get_data()
                update_selected_condition(user_id=message.from_user.id, nft_name=curr_data_of_states['name'], condition=curr_data_of_states['condition'],
                                          value=curr_data_of_states['value_of_condition'])
                await state.finish()
    except ValueError as e:
        logger.debug(f'Value is not correct: {message.text}; error: {e}')
        curr_data_of_states = await state.get_data()
        print(curr_data_of_states)
        if 'value_of_condition' in curr_data_of_states:
            await state.update_data(value_of_condition=curr_data_of_states['value_of_condition'] - 1)
            if curr_data_of_states['value_of_condition'] <= numb_of_failed_attempts:
                await message.answer(text='ТЕРПЕНИЯ НОЛЬ ЭБАТЬ. АТМЕНА')
                await state.reset_state()
                return
        else:
            await state.update_data(value_of_condition=-1)
        await message.reply(text='Value is not correct. Try again.')
