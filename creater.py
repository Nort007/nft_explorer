from db.banned.model import BanModel
from db.base.base_model import psql_db
from db.conditions.model import ConditionModel
from db.mailing.model import MailingModel
from db.profiles.model import ProfileModel
from db.profiles_watchlist.model import ProfileWatchlistModel
from db.watchlist.model import WatchlistModel

if __name__ == '__main__':
    psql_db.create_tables([
        ProfileModel,
        WatchlistModel,
        ProfileWatchlistModel,
        BanModel,
        ConditionModel,
        MailingModel], safe=True)
