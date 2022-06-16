import redis

from core.config import REDIS_HOST, REDIS_PORT

redis_app = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
