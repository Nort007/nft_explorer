import time
import requests
import json


def additional_payload(val):
    pass


def gem_aggregator(url: str, header: dict, payload: dict):
    with requests.Session() as session:
        session.headers.update(header)
        options_response = session.options(url)
        if options_response.status_code == 204:
            session.headers.update({'method': 'POST'})
        time.sleep(0.578)
        post_response = session.post(url, json=payload)
        if post_response.status_code == 200:
            # print(post_response.text)
            return post_response.json()


options_header = {
    'authority': 'api-4.gemlabs.xyz',
    'method': 'OPTIONS',
    'path': '/collections',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'access-control-request-headers': 'content-type, x-api-key',
    'access-control-request-method': 'POST',
    'dnt': '1',
    'origin': 'https://www.gem.xyz',
    'referer': 'https://www.gem.xyz/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

post_header = {
    'Referer': 'https://www.gem.xyz/',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
}
url = 'https://search.gemlabs.xyz/search'

payload = {
   "filters": {
      "searchText": "lil pudgys"
   },
   "limit": 25,
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


if __name__ == '__main__':
    t = gem_aggregator(url, header=options_header, payload=payload)
    print(json.dumps(t, indent=4))
