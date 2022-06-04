from selenium.common.exceptions import NoSuchElementException

from bot_v01.misc import logger
from .aggregator_data import GemAggregator, HEADER, PAYLOAD
from .gem_information import Gem
from .gem_scrapper import GemScrapper


# from general_tools import BaseDisplay


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


def gem_collection(addr: str):
    gem = GemScrapper(addr)
    driver = gem.start()
    # disp = BaseDisplay()
    try:
        req = driver.get(gem.by_collection_address())
        driver.implicitly_wait(10)
        response = gem.response_information()
        return response
    except Exception as e:
        logger.error(f"gem_collection: {e.args}")
        pass
    driver.quit()
    # disp.stop_display()
