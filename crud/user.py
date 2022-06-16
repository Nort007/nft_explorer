from db.profiles.model import ProfileModel


def get_users(skip: int = 0, limit: int = 100):
    return list(ProfileModel.select().offset(skip).limit(limit))
