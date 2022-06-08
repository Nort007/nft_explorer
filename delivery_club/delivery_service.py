from bot_v01.services import disclosure_fully_infromation_of_users


def information_nft_channels_and_groups() -> dict:
    """Getting all groups and channels of users and sorting by NFT.
    """
    gc_dict = {}
    datas = list(disclosure_fully_infromation_of_users().dicts())
    for i in range(len(datas)):
        datas[i].update(name=datas[i]['name'].replace(' ', '_').lower())
    for data in datas:
        chat = str(data['chat_id']) if data['chat_id'] else '@' + str(data['public_channel'])
        if data['name'] in gc_dict.keys():
            cnt = gc_dict[data['name']]['results'] + 1
            gc_dict[data['name']]['results'] = cnt
            gc_dict[data['name']]['chats'].append(chat)
            gc_dict[data['name']].update({chat: {'conditions': {
                'gt': data['gt'],
                'ge': data['ge'],
                'lt': data['lt'],
                'le': data['le'],
                'eq': data['eq']
            }}})
        elif data['name'] not in gc_dict.keys():
            gc_dict[data['name']] = {
                'address': data['address'],
                'slug': data['slug'],
                'results': 1,
                'chats': [chat],
                chat: {
                    'conditions': {
                        'gt': data['gt'],
                        'ge': data['ge'],
                        'lt': data['lt'],
                        'le': data['le'],
                        'eq': data['eq']
                    }
                }
            }
    return gc_dict


async def send_message_by_condition(**kw):
    """
    :param nft:
    :param gt:
    :param lt:
    :param eq:
    :param chat_id:
    :param floor:
    """
    message = f"NFT: **{kw.get('nft')}**\n"
    if kw.get('gt') is not None and kw.get('floor') > kw.get('gt'):
        message += f"Floor price {kw.get('floor')} is greater(📈) than your price {kw.get('gt')}"
        await kw.get('bot').send_message(chat_id=kw.get('chat_id'), text=message)
    if kw.get('lt') is not None and kw.get('floor') < kw.get('lt'):
        message += f"Floor price {kw.get('floor')} is less(📉) than your price {kw.get('lt')}"
        await kw.get('bot').send_message(chat_id=kw.get('chat_id'), text=message)
    if kw.get('eq') is not None and kw.get('floor') == kw.get('eq'):
        message += f"Floor price {kw.get('floor')} is equal(🎰) to your price {kw.get('eq')}"
        await kw.get('bot').send_message(chat_id=kw.get('chat_id'), text=message)
    # await bot.close()
