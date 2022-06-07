from bot_v01.misc import logger
from .aggregator_data import GemAggregator, HEADER, PAYLOAD
from .gem_scrapper import GemScrapper


def information_by_name(name: str):
    """Gives information about nft by name."""
    gem_by_name = GemAggregator(header=HEADER, payload=PAYLOAD, name=name)
    return gem_by_name.get_response()


def gem_collection(addr: str):
    """Gives information about nft collection by address."""
    gem = GemScrapper(addr)
    driver = gem.start()
    try:
        req = driver.get(gem.by_collection_address())
        driver.implicitly_wait(10)
        response = gem.response_information()
        return {'name': response['data'][0]['name'],
                'address': response['data'][0]['address'],
                'slug': response['data'][0]['slug']}
    except Exception as e:
        logger.error(f"gem_collection: {e.args}")
        pass
    driver.quit()
