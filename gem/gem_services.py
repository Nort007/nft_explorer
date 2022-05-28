from selenium.common.exceptions import NoSuchElementException
from .gem_information import Gem
from bot_v01.misc import logger
from .aggregator_data import GemAggregator, HEADER, PAYLOAD


def information_by_address(addr: str):
    gem = Gem(addr)
    driver = gem.start()
    try:
        driver.get(gem.by_collection_address())
        driver.implicitly_wait(10)
        information = gem.initial_information_by_tag()
        return information
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e.args}")
        return False


def information_by_name(name: str):
    gem_by_name = GemAggregator(header=HEADER, payload=PAYLOAD, name=name)
    return gem_by_name.get_response()
