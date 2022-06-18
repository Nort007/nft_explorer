import os
import random
from base64 import b64encode
from pathlib import Path

import dotenv

KEY_VARIABLES = (
    'JWT_SECRET_KEY',
)

ENV_FILE = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env.example')


def generate_password(length=64):
    return b64encode(random.randbytes(length)).decode()


def generate_env_file():
    for key_var in KEY_VARIABLES:
        dotenv.set_key(ENV_FILE, key_var, generate_password(), quote_mode='never')


if __name__ == "__main__":
    generate_env_file()
