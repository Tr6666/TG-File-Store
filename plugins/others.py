from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.incoming & filters.channel)
async def button_post(c, m):
    chat = await c.get_chat(m.chat.id)

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Join', url=chat.invite_link.lower()),
            InlineKeyboardButton('More Updates', url='t.me/t2links')
        ]
    ])

    await m.edit(m.text + ".", entities=m.entities, reply_markup=buttons, disable_web_page_preview=True)
