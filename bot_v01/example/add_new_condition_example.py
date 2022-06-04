from db.conditions.model import ConditionModel


def add_new_condition():
    q = ConditionModel(profile_id=1, watchlist_id=2, le=0.94)
    q.save()


# add_new_condition()
