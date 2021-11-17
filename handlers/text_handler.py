from aiogram import types
from misc import dp,bot
import asyncio



My_id = 494588959
channel_posts = -1001584434154
#{"id": -1001405664089, "title": "Проверка учасника", "username": "movie_bots", "type": "channel"}


@dp.message_handler(content_types='text')
async def all_other_messages(message: types.message):
    print(message)
    a = await bot.copy_message(chat_id= channel_posts, message_id= message.message_id, from_chat_id=message.chat.id)