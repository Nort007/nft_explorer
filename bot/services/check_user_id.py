import asyncio
import json
from pathlib import Path
import os


path = Path(os.path.dirname(os.path.abspath(__file__))).resolve().joinpath('permission.json')


def compare_user_id_from_db(user_id):
    """Сравнивает есть ли юзер в базе данных или нет."""
    with open(path, 'r') as r:
        data = json.load(r)
    if user_id in data['users']:
        print('User has been found')
        # return True
        return True
    else:
        return False
