import requests
import json


def additional_payload(val):
    pass


def gem_aggregator(url: str, headers: dict, payload: dict):
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.post(url, json=payload)
        if response.status_code == 200:
            return response.json()


headers = {
    'Referer': 'https://www.gem.xyz/',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
}
url = 'https://nft-aggregator-api.herokuapp.com/collections'
payload = {
    "sort": {
        "oneDayVolume": "desc"
    },
    "fields": {
        "name": 1,
        "symbol": 1,
        "standard": 1,
        "description": 1,
        "address": 1,
        "createdDate": 1,
        "externalUrl": 1,
        "imageUrl": 1,
        "totalSupply": 1,
        "sevenDayVolume": 1,
        "oneDayVolume": 1,
        "stats": 1,
        "indexingStatus": 1,
        "discordUrl": 1,
        "instagramUsername": 1,
        "isVerified": 1,
        "lastNumberOfUpdates": 1,
        "lastOpenSeaCancelledId": 1,
        "lastOpenSeaSaleCreatedId": 1,
        "slug": 1,
        "lastOpenSeaTransferId": 1,
        "lastRaribleAssetUpdateId": 1,
        "mediumUsername": 1,
        "telegramUrl": 1,
        "twitterUsername": 1,
        "updatedAt": 1,
        "wikiUrl": 1
    },
    "limit": "100",
    "filters": {"address": "0x524cab2ec69124574082676e6f654a18df49a048"}
}

if __name__ == '__main__':
    t = gem_aggregator(url, headers, payload)
    print(json.dumps(t, indent=4))
