from db.profiles import model


def get_user(user_id: int):
    return model.ProfileModel.filter(model.ProfileModel.user_id == user_id).first()
