import aiohttp

from gem import HEADER, PAYLOAD, URL


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
