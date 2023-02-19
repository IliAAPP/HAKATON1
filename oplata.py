# бот по оплате счетов единым платежом!
import telebot
from telebot import types

bot = telebot.TeleBot("5393443331:AAGR0oWPRFIM3eTofvmXkAFTexL0ZrP_99E")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Юмани")
    btn2 = types.KeyboardButton("JustClick")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}🤗! Привет! Предлагаю тебе оплатить коммунальный услуги единым платежом следующими способами:- ЮMoney".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Вернуться назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Юмани")
        btn2 = types.KeyboardButton("JustClick")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}🤗! Привет! Предлагаю тебе оплатить коммунальный услуги единым платежом следующими способами:- ЮMoney".format(
                             message.from_user), reply_markup=markup)
    if (message.text == "Юмани"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="ПРЕДУПРЕЖДЕНИЕ! ПОСЛЕ ПЕРЕХОДА ПО ССЫЛКЕ С ВАС СПИШЕТСЯ УКАЗАНАЯ СУММА",
                         reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Оплатить в один клик!", url='https://app.leadteh.ru/w/e2fa')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Ссылка на оплату: https://app.leadteh.ru/w/e2fa", reply_markup=markup)


bot.polling(none_stop=True)
