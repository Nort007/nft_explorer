from .service_db import add_or_update_mailing, get_user_information


def prepare_channel_or_group(chat: str, profile_id: int):
    """:param chat: require
    :type chat:
    :param profile_id: require
    :type profile_id:
    :return:
    :rtype:"""
    user = get_user_information(profile_id).get()
    d = ['one', 'two', 'three']
    datas = {'chat_id': None, 'public_channel': None, 'active': False}
    if chat.startswith('-') and chat[1:].isdigit():
        datas.update(chat_id=chat, active=True)
    else:
        datas.update(public_channel=chat)
    return add_or_update_mailing(public_channel=datas['public_channel'], chat_id=datas['chat_id'], active=datas['active'], user_pk_id=user.id)
