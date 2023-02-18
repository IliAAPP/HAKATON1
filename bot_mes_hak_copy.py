# бот для жильцов и сотрудников комплексов, предназначенный
# для своевременного оповещения жильцов и сотрудников о предстоящих
# событиях

import sqlite3
import telebot
from datetime import datetime

bot = telebot.TeleBot("6207892033:AAHEVAwjsxeUH-_HnbaiIEZJEg2GMJAL3s0")

conn = sqlite3.connect("C:\db\database.db", check_same_thread=False)
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Зарегистрируй свои данные с помощью слова "Авторизоваться"')
    bot.send_message(message.chat.id, 'Чтобы узнать о том, что умеет бот НАЖМИ /help')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '''
    Привет! Доступны следующие команды:
    /sign - авторизоваться
    /get_mes - получить сообщение - напоминалку
    /input_mes - записать напоминание 
    ''')


@bot.message_handler(commands=['input_mes'])
def input_mes(message):
    d = bot.send_message(message.chat.id, 'Введи сообщение, которое нужно сохранить для напоминания!')
    a = bot.register_next_step_handler(d, inp)


# @bot.message_handler(commands=['input_mes'])
# def input_mes(message):
#     d = bot.send_message(message.chat.id, 'Введи город')
#     a = bot.register_next_step_handler(d, inp)
#     b = message.chat.id
#     cursor.execute(f"UPDATE test SET mes = {a} WHERE mes = {b}")
#     conn.commit()
#
#
def inp(message):
    bot.send_message(message.chat.id, 'Записываю напоминание "{inp}" в базу данных...'.format(inp=message.text))
    bot.send_message(message.chat.id, "Успешно!")


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['get_mes'])
def get_mes(message):
    b = message.chat.id
    a = cursor.execute(f'SELECT mes FROM test where user_id = {b}')
    bot.send_message(message.chat.id, a)
    conn.commit()


@bot.message_handler(commands=['sign'])
def get_text_messages(message):
    bot.send_message(message.chat.id, 'Привет! Ваши данные добавлены в базу данных!')
    try:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    except sqlite3.IntegrityError:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы в системе!')


bot.polling(none_stop=True)
