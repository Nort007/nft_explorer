from bot_v01.services import disclosure_fully_infromation_of_users


def all_channels_groups() -> dict:
    """
    Получение всех групп и каналов пользователей и сортировка их.
    :return:
    """
    gc_dict = {}
    datas = list(disclosure_fully_infromation_of_users().dicts())
    for i in range(len(datas)):
        datas[i].update(name=datas[i]['name'].replace(' ', '_').lower())
    for data in datas:
        chat = str(data['chat_id']) if data['chat_id'] else str(data['public_channel'])
        if data['name'] in gc_dict.keys():
            cnt = gc_dict[data['name']]['results'] + 1
            gc_dict[data['name']]['count'] = cnt
            gc_dict[data['name']].update({chat: {'conditions': {
                'gt': data['gt'],
                'ge': data['ge'],
                'lt': data['lt'],
                'le': data['le'],
                'eq': data['eq']
            }}})
        elif data['name'] not in gc_dict.keys():
            gc_dict[data['name']] = {
                'results': 1,
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
