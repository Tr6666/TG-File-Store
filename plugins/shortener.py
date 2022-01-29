from pyrogram import Client, filters
import aiohttp

chat = [1166625664, 2132021818, 1383296549]


@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.private & filters.chat(chat))
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'`{short_link}`', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://droplink.co/api'
    params = {'api': "1aab74171e9891abd0ba799e3fd568c9598a79e1", 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            return data["shortenedUrl"]
