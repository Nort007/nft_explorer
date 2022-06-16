from celery import Celery

from core.config import REDIS_HOST, REDIS_PORT

BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
celery_app = Celery('worker', broker=BROKER_URL)
celery_app.conf.task_routes = {
    'api.celery_worker.send_code': 'main_queue',
    'api.celery_worker.celery_put_in_redis': 'main_queue'
}
