import re
import aiohttp
from pyrogram import Client, filters
import requests
import emoji
chat = [1166625664, 2132021818, 1383296549]

# ##################################  droplink  #################################################################


@Client.on_message(filters.command('dp') & filters.chat(chat))
async def reply_text(c, m):
    try:
        text = await m.reply_text("`Processing...... May take some time`")
        try:
            txt = await bulk_shortener(m.reply_to_message.text)
            r = f"**{txt}**\n\n**@T2links**"
            await m.reply_text(r)
        except:
            txt = await bulk_shortener(m.reply_to_message.caption)
            id = m.reply_to_message.photo.file_id
            r = f"**{txt}**\n\n**@T2links**"
            await m.reply_photo(id, caption=r)
        await text.delete()
    except:
        await text.delete()
        await m.reply_text("`Some Error Occurred, Use this command only to short your links to Droplink url`")


async def bulk_shortener(message):
    emoji_text = message.split()

    for emojis in emoji_text:
        isEmoji = emoji.is_emoji(emojis)
        if isEmoji is True:
            message = message.replace(emojis, "")
        else:
            pass
    urls = re.findall(r'https?://[^\s]+', message)
    for url in urls:
        short_link = await get_shortlink(url)
        short_link = f"[👉 Link 🔗]({short_link})"
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


# ##################################  Mdisk  #################################################################


@Client.on_message(filters.command('mdisk') & filters.chat(chat))
async def mdisk(c, m):
    try:
        text = await m.reply_text("`Processing...... May take some time`")
        try:
            txt = await mdisk_bulk_shortener(m.reply_to_message.text)
            r = f"**{txt}**\n\n**@T2links**"
            await m.reply_text(r)
        except:
            txt = await mdisk_bulk_shortener(m.reply_to_message.caption)
            id = m.reply_to_message.photo.file_id
            r = f"**{txt}**\n\n**@T2links**"
            await m.reply_photo(id, caption=r)
        await text.delete()
    except:
        await text.delete()
        await m.reply_text("`Some Error Occurred, Reply only to MDisk links`")


async def mdisk_bulk_shortener(message):
    urls = re.findall(r'https?://[^\s]+', message)
    for url in urls:
        mdisk_link = await get_mdisk(url)
        mdisk_link = f"[👉 Link 🔗]({mdisk_link})"
        if url in message:
            message = message.replace(url, mdisk_link)

    emoji_text = message.split()

    for emojis in emoji_text:
        isEmoji = emoji.is_emoji(emojis)
        if isEmoji is True:
            message = message.replace(emojis, "")
        else:
            pass

    return message


async def get_mdisk(link):
    url = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
    param = {'token':
                 '6LZq851sXoPHuwqgiKQq', 'link': link
             }
    res = requests.post(url, json=param)
    shareLink = res.json()
    return shareLink["sharelink"]


######################################## Mdisk and droplink #######################################################


@Client.on_message(filters.command('shorten') & filters.chat(chat))
async def shorten(c, m):
    try:
        text = await m.reply_text("`Converting other MDisk links to your MDisk account... May take some time`")
        try:
            txt = await mdisks_bulk_shortener(m.reply_to_message.text)
            await text.edit(
                "Converted all links to your MDisk account. Now converting all your MDisk links to droplink url.....")
            txt = await bulk_shortener(txt)
            r = f"**{txt}**\n\n**@T2links**"
            await m.reply_text(r)
        except:
            txt = await mdisks_bulk_shortener(m.reply_to_message.caption)
            txt = await bulk_shortener(txt)
            id = m.reply_to_message.photo.file_id
            r = f"**{txt}**\n\n**@T2links**"
            await m.reply_photo(id, caption=r)
        await text.delete()
    except:
        await text.delete()
        await m.reply_text("`Some Error Occurred, Reply only to MDisk links`")


async def mdisks_bulk_shortener(message):
    urls = re.findall(r'https?://[^\s]+', message)
    for url in urls:
        mdisk_link = await get_mdisk(url)
        if url in message:
            message = message.replace(url, mdisk_link)

    emoji_text = message.split()

    for emojis in emoji_text:
        isEmoji = emoji.is_emoji(emojis)
        if isEmoji is True:
            message = message.replace(emojis, "")
        else:
            pass

    return message
