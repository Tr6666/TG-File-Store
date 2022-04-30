from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
import asyncio

CHAT = [-1001793534052, -1001400526156, -1001230546236, -1001286887151, -1001751988620, -1001172494089, -1001781675464,
        -1001348118571, -1001242897508, -1001519791986, -1001730250578, -1001205374653, -1001726864577, -1001573047911]

dicts = []


@Client.on_message(filters.incoming & filters.channel & filters.edited & filters.chat(CHAT))
async def button_post(c, m):
    await asyncio.sleep(60)
    global dicts
    message_id = m.message_id
    chat_id = m.chat.id
    dic = {
        'message_id': message_id,
        'chat_id': chat_id
    }
    dicts.append(dic)
    
    if m.text:
        chat = await c.get_chat(m.chat.id)

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('Join', url=chat.invite_link),
                InlineKeyboardButton('More Updates', url='https://t.me/T2linksAnnc')
            ]
        ])

        await m.edit(m.text, entities=m.entities, reply_markup=buttons, disable_web_page_preview=True)
        
        
@Client.on_message(filters.command('del'))
async def auto_delete(c: Client, m: Message):
    await asyncio.sleep(60)
    txt = await m.reply_text("Deleting")
    global dicts
    messages = dicts
    for message in messages:
        await c.delete_messages(chat_id=message["chat_id"], message_ids=int(message["message_id"]))
    dicts = []
    await txt.edit("Deleted")
        
        
        
@Client.on_message(filters.incoming & filters.channel & filters.edited & filters.chat(-1001667892071))
async def main_channel_button_post(c, m):  
        await asyncio.sleep(60)
        if m.text:
                        
          chat = await c.get_chat(m.chat.id)

          buttons = InlineKeyboardMarkup([
              [
                  InlineKeyboardButton('Join', url=chat.invite_link),
                  InlineKeyboardButton('More Updates', url='https://t.me/T2linksAnnc')
              ]
          ])

          await m.edit(m.text, entities=m.entities, reply_markup=buttons, disable_web_page_preview=True)
