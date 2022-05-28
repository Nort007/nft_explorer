import json
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
    "limit": 5,
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
    },
}


class GemAggregator:
    def __init__(self, header: dict, payload: dict, name: str = None, by_name: bool = True):
        self.payload = payload
        self.header = header
        self.name = name
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

    def _response(self):
        if self.by_name:
            self.__prepare_session_by_name()
            self.__prepare_payload()
        response = self.session.post(data.url, json=self.payload)
        if response.status_code == 200:
            return response.json()

    def get_response(self):
        response = self._response()
        if len(response['data']['collections']) > 0:
            for data in response['data']['collections']:
                if data['slug'] == self.name or data['name'] == self.name:
                    return data
        else:
            return False
