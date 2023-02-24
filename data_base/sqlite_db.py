import sqlite3 as sq
from create_bot import bot

from utils.logger import logging

def sql_start():
    global base, cur
    
    try:
        logging.info(f'Try to connect to sqlite3 data base')
        base = sq.connect('test_data.db')
        cur = base.cursor()
        logging.info(f'Connect to data base {base} done')
    except Exception as e:
        logging.error(f'Can not connect to the databace. {e}')

    base.execute('CREATE TABLE IF NOT EXISTS test_table(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        try:
            logging.info(f'Try to insert data to the test_table')
            cur.execute('INSERT INTO test_table VALUES (?, ?, ?, ?)', tuple(data.values()))
            base.commit()
            logging.info(f'Isert data to the test_table done')
        except Exception as e:
            logging.info(f'Can not insert data {tuple(data.values())} on test_table')

async def sql_select_all(message):
    for ret in cur.execute('SELECT * FROM test_table').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
