import asyncio

from bot_v01.misc import bot
from delivery_service import information_nft_channels_and_groups, send_message_by_condition
from general_tools import user_agent as fake_agent
from session_service import get_post_datas, custom_payload


async def main():
    get_info = information_nft_channels_and_groups()
    nfts = [name.replace('_', ' ') for name in get_info.keys()]
    slugs = [v['slug'] for k, v in get_info.items()]
    futures = [get_post_datas(fake_user_agent=fake_agent(), payload=custom_payload(nft)) for nft in nfts]
    for i, future in enumerate(asyncio.as_completed(futures)):
        results = await future
        if results['data']['collections'][0]['slug'] in slugs:
            """If the slug from db as equal as in response from api."""
            floor = results['data']['collections'][0]['stats']['floor_price']
            name = results['data']['collections'][0]['name']

            chats = get_info[name.replace(' ', '_').lower()]['chats']
            for chat in chats:
                conditions = get_info[name.replace(' ', '_').lower()][chat]['conditions']
                await send_message_by_condition(nft=name, gt=conditions['gt'], lt=conditions['lt'], eq=conditions['eq'], chat_id=chat, floor=floor, bot=bot)
    await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
