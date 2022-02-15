from pyrogram import Client, filters
from pyrogram.types import Message

CHAT = [-1001793534052, -1001400526156, -1001230546236, -1001286887151, -1001751988620, -1001172494089, -1001781675464,
        -1001348118571, -1001242897508, -1001519791986, -1001730250578, -1001205374653, -1001726864577]

dicts = []


@Client.on_message(~filters.command('del') & filters.chat(CHAT) & filters.channel & ~filters.edited)
async def save_message_id(c: Client, m: Message):
    global dicts
    message_id = m.message_id
    chat_id = m.chat.id
    dic = {
        'message_id': message_id,
        'chat_id': chat_id
    }
    dicts.append(dic)


@Client.on_message(filters.command('del'))
async def auto_delete(c: Client, m: Message):
    txt = await m.reply_text("Deleting")
    global dicts
    messages = dicts
    for message in messages:
        await c.delete_messages(chat_id=message["chat_id"], message_ids=int(message["message_id"]))
    dicts = []
    await txt.edit("Deleted")

