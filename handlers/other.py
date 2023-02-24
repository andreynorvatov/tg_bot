from aiogram import Dispatcher, types
import random

import string, json

from create_bot import dp
from handlers.messages import *


# @dp.message_handler()
async def cenz_message_check(message : types.Message):  
    # with open('cenz.json', 'r') as f:
    #     for i in f:
    #         print(i)
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('utils/cenz.json')))) != set():
            await message.reply(random.choice(MESSAGE_CENZ))
            await message.delete()


# async def startswith_slash_check(message : types.Message):
    elif message.text.startswith('\\'):
        await message.reply(MESSAGE_SLASH)





def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(cenz_message_check)
    # dp.register_message_handler(startswith_slash_check)
    
