import unittest
from peewee import SqliteDatabase
from db.profiles.model import ProfileModel


dbase = SqliteDatabase(':memory:')
MODELS = [ProfileModel]


class TestProfile(unittest.TestCase):
    def setUp(self):
        dbase.bind(MODELS, bind_refs=False, bind_backrefs=False)
        dbase.connect()
        dbase.create_tables(MODELS)

    def tearDown(self) -> None:
        dbase.drop_tables(MODELS)
        dbase.close()

    def test_add_new_profile(self):
        profile = ProfileModel.create(is_bot=False, first_name='John', username='qwerty', lang_code='en', user_id=123)
        profile.save()
        assert profile
