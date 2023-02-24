from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

storage = MemoryStorage()

# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token='5399291638:AAEM6kqZ3CfbmixMzZj9gV962QaDPhPe87U')


dp = Dispatcher(bot, storage=storage)


