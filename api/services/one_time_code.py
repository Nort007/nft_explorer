import random


def get_one_time_code():
    """The simple functions of implementing a one-time code."""
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return "".join([str(l.pop(random.randint(0, len(l) - 1))) for _ in range(6)])
