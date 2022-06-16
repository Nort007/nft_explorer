from db.profiles import model


def get_users(skip: int = 0, limit: int = 100):
    return list(model.ProfileModel.select().offset(skip).limit(limit))


def get_user(username: str = None, user_id: int = None):
    if username is not None:
        return model.ProfileModel.filter(model.ProfileModel.username == username).first()
    if user_id is not None:
        return model.ProfileModel.filter(model.ProfileModel.user_id == user_id).first()
