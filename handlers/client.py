from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
import random

from create_bot import dp, bot
from data_base import sqlite_db
from keyboards import kb_client
from handlers.messages import *


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, random.choice(MESSAGE_HELLO), reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply(MESSAGE_FIRST)

async def command_help(message:  types.Message):
	await message.answer(MESSAGE_HELP)
	# await message.delete()

async def test_table_view(message: types.Message):
	await sqlite_db.sql_select_all(message)



def register_handlers_client(dp: Dispatcher):
	dp.register_message_handler(command_start, Text(equals=['start'], ignore_case=True))
	dp.register_message_handler(command_help, Text(equals=['help', 'помощь', 'справка'], ignore_case=True))
	dp.register_message_handler(test_table_view, lambda message: 'Select * from test_table' in message.text)

