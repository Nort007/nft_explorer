import aiohttp

from core.config import TELEGRAM_API, TELEGRAM_TOKEN
from core.logger_config import logger


async def send_message(chat_id: int, msg: str):
    url = f"{TELEGRAM_API}bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    logger.debug('initial sending message, : %s, %s', chat_id, msg)
    async with aiohttp.ClientSession() as session:
        logger.debug('Session: %s', session)
        async with session.get(url) as response:
            logger.debug(f'Response: {response} status: {response.status}')
            return response.status
