from pyrogram import Client, filters
import aiohttp
import re

chat = [1166625664, 2132021818, 1383296549]


@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.chat(chat))
async def reply_text(c,m):
    text = await m.reply_text("Processing")
    try:
        txt = await bulk_shortener(m.text)
        await m.reply_text(txt)
    except:
        txt = await bulk_shortener(m.caption)
        id = m.photo.file_id
        await m.reply_photo(id, caption=f"**{txt}**")
    await text.delete()


async def bulk_shortener(message):
    urls = re.findall(r'https?://[^\s]+', message)
    for url in urls:
        short_link = await get_shortlink(url)
        if url in message:
            message = message.replace(url, short_link)

    return message


async def get_shortlink(link):
    url = 'https://droplink.co/api'
    params = {'api': "1aab74171e9891abd0ba799e3fd568c9598a79e1", 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            return data["shortenedUrl"]
