from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('Start')
button_2 = KeyboardButton('Help')
button_3 = KeyboardButton('Тест фильтра мата (кот)')
button_4 = KeyboardButton('Поделиться номером', request_contact=True)
button_5 = KeyboardButton('Отправить где я', request_location=True)
button_6 = KeyboardButton('Select * from test_table')
button_7 = KeyboardButton('AWR_analizer')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# kb_client.add(button_1).add(button_2).insert(button_3)
kb_client.row(button_1, button_2)
kb_client.row(button_3)
kb_client.row(button_4, button_5)
kb_client.row(button_6, button_7)
