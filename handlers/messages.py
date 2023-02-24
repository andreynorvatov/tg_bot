import aiogram.utils.markdown as fmt

'''---------------CLIENT MESSAGES---------------'''

MESSAGE_HELLO = ['Привет!', 'Рад тебя видеть))', 'Погнали!!!', 'Чем могу помочь?']
MESSAGE_FIRST = 'Общение с ботом через ЛС, напиши ему :\nhttps://t.me/LoadTest_PyBot'
MESSAGE_HELP = fmt.text(
    fmt.text(fmt.hbold('Вы вызвали справку'),
    'Этот бот что-то умеет',
    fmt.link(title='Гугл', url='http://www.google.com/'),
    sep= '\n'
    ))

"""
<b>Вы вызвали справку</b>.
Сообщение с <u>HTML-разметкой</u>
Этот бот что-то умеет.\n
Проверка переноса строки.\n
\satart попробуй нажать
[ссылка](http://www.google.com/)
"""

'''---------------ADMIN MESSAGES---------------'''
MESSAGE_HELLO_ADMIN = 'Вы вошли в административный режим бота.'
MESSAGE_CM_START_ADMIN = 'Загрузи фото'

'''---------------OTHER MESSAGES---------------'''

MESSAGE_CENZ = ['Мат запрещен!', 'Материться не надо', 'Сработал фильтр мата, сообщение удалено']
MESSAGE_SLASH = 'Команда должна начинаться со слеша /'