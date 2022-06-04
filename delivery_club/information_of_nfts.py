import asyncio
import json

import aiohttp

from gem import HEADER, PAYLOAD, URL
from general_tools import user_agent as fake_agent


def custom_payload(nft: str):
    payload = PAYLOAD.copy()
    payload.update(filters={'searchText': nft})
    return payload


async def get_post_datas(payload, fake_user_agent: str = None):
    async with aiohttp.ClientSession() as session:
        session.headers.update(HEADER)
        if fake_user_agent:
            session.headers.update({'User-Agent': fake_user_agent})
        async with session.post(URL, json=payload) as response:
            datas = await response.json()
        return datas


async def main():
    nfts = ['lil pudgys', 'Sorare', 'Boki', 'goblintown.wtf']
    futures = [get_post_datas(fake_user_agent=fake_agent(), payload=custom_payload(nft)) for nft in nfts]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print(json.dumps(result['data']['collections'], indent=4, default=str))


if __name__ == '__main__':
    asyncio.run(main())
