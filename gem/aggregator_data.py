import time
import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from pydantic import BaseModel
from random import uniform


env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)


class Components(BaseModel):
    """Class to create a header for the request"""
    authority: str = os.getenv('GEMXYZ_AUTHORITY')
    origin: str = os.getenv('GEMXYZ_URL')
    referer: str = os.getenv('GEMXYZ_URL') + '/'
    url: str = os.getenv('GEMLAB_URL')


component = Components()
HEADER = {
    'authority': component.authority,
    'method': 'OPTIONS',
    'path': '/collections',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'access-control-request-headers': 'content-type, x-api-key',
    'access-control-request-method': 'POST',
    'dnt': '1',
    'origin': component.origin,
    'referer': component.referer,
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}
PAYLOAD = {
   "limit": 2,
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


def generate_payload(default_payload: dict, params: dict) -> dict:
    # {"filters": {'searchText': 'Lil pudgys'}}
    default_payload.update(params)
    return default_payload


def gem_aggregator(url: str, header: dict, payload: dict):
    with requests.Session() as session:
        session.headers.update(header)
        options_response = session.options(url)
        if options_response.status_code == 204:
            session.headers.update({'method': 'POST'})
        time.sleep(round(uniform(0.300, 0.700), 3))
        post_response = session.post(url, json=payload)
        if post_response.status_code == 200:
            return post_response.json()


def send_request(additional_payload: dict, url: str = component.url, header: dict = HEADER, payload: dict = PAYLOAD):
    payload = generate_payload(default_payload=payload, params=additional_payload)
    return gem_aggregator(url=url, header=header, payload=payload)
