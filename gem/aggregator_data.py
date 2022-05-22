import time
import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from pydantic import BaseModel
from random import uniform, randint


env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)


class Components(BaseModel):
    """Class to create a header for the request"""
    authority: str = os.getenv('GEMXYZ_AUTHORITY')
    origin: str = os.getenv('GEMXYZ_URL')
    referer: str = os.getenv('GEMXYZ_URL') + '/'
    url: str = os.getenv('GEMLAB_URL')


data = Components()
URL = data.url
HEADER = {
    'authority': data.authority,
    'path': '/search',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'access-control-request-headers': 'content-type, x-api-key',
    'access-control-request-method': 'POST',
    'dnt': '1',
    'origin': data.origin,
    'referer': data.referer,
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
}
PAYLOAD = {
   "limit": 1,
   "fields": {
      "name": 1,
      "symbol": 1,
      "standard": 1,
      "description": 1,
      "address": 1,
      "tokenId": 1,
      "createdDate": 1,
      "externalUrl": 1,
      "id": 1,
      "imageUrl": 1,
      "totalSupply": 1,
      "sevenDayVolume": 1,
      "oneDayVolume": 1,
      "stats": 1,
      "indexingStatus": 1,
      "discordUrl": 1,
      "slug": 1,
      "isVerified": 1,
      "lastNumberOfUpdates": 1,
      "lastOpenSeaCancelledId": 1,
      "lastOpenSeaSaleCreatedId": 1,
      "lastOpenSeaTransferId": 1,
      "lastRaribleAssetUpdateId": 1
   }
}


def generate_payload(default_payload: dict = PAYLOAD, params: dict = None) -> dict:
    # {"filters": {'searchText': 'Lil pudgys'}}
    default_payload.update(params)
    return default_payload


def gem_aggregator(url: str, header: dict, payload: dict):
    with requests.Session() as session:
        session.headers.update(header)
        options_response = session.options(url)
        print(options_response.status_code)
        if options_response.status_code == 200:
            session.headers.update({'method': 'POST'})
        time.sleep(round(uniform(0.300, 0.700), 3))
        post_response = session.post(url, json=payload)
        print(post_response.status_code)
        if post_response.status_code == 200:
            return post_response


def send_request(payload: dict, url: str = data.url, header: dict = HEADER):
    return gem_aggregator(url=url, header=header, payload=payload)


def gem_agg_only_post(url: str, header: dict, payload: dict):
    with requests.Session() as session:
        session.headers.update(header)
        # session.headers.update({'method': 'POST'})
        post_response = session.post(url, json=payload)
        return post_response


class GemException(BaseException):
    def __init__(self, m):
        self.msg = m

    def __str__(self):
        return self.msg


class GemAggregator:
    def __init__(self, header: dict, payload: dict, name: str = None, address: str = None, by_name: bool = True):
        self.payload = payload
        self.header = header
        self.name = name
        self.address = address
        self.by_name = by_name
        self.session = requests.Session()

    def __header_for_search(self):
        self.header.update({'method': 'POST'})
        self.header.update({'authority': 'search.gemlabs.xyz'})
        self.header.update({'path': '/search'})

    def __prepare_payload(self):
        self.payload.update(filters={'searchText': self.name})

    def __prepare_session_by_name(self):
        self.__header_for_search()
        self.session.headers.update(self.header)

    def __prepare_session_by_address(self):
        self.__header_for_search()
        self.session.headers.update(self.header)
        self.payload.update(filters={'address': self.address})

    def get_response(self):
        if self.by_name:
            self.__prepare_session_by_name()
            if self.name is None:
                raise GemException('Name is None')
            self.__prepare_payload()
            response = self.session.post(data.url, json=self.payload)
            print(self.session.headers)
            if response.status_code == 200:
                return response.json()

    


t = GemAggregator(header=HEADER, payload=PAYLOAD, name='Lil pudgys')
print(t.get_response())