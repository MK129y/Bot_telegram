import random
import telebot
import requests
from bot_token import bot_one #api bot 
from telebot import types as ty


@bot_one.message_handler(commands=['start'])
def welcome(message):
    sti = open('gerl.webp', 'rb')
    bot_one.send_sticker(message.chat.id, sti)

    # keyboard
    markup = ty.ReplyKeyboardMarkup(resize_keyboard=True)

    bot_one.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot_one.get_me()),
                     parse_mode='html', reply_markup=markup)
    
    #КНОПКИ
@bot_one.message_handler(commands=['get_info','info'])
def get_info(message):
    markup_inline = ty.InlineKeyboardMarkup(row_width= 2); #row_width=сколько кнопок в ряд
    itemp1_yes = ty.InlineKeyboardButton(text='Да', callback_data='yes_1')
    itemp2_no = ty.InlineKeyboardButton(text='Нет', callback_data='no_1')#callback_data='id переменной??
    itemp3_yes = ty.InlineKeyboardButton(text='Надор подумать', callback_data='yes_2')
    itemp4_yes = ty.InlineKeyboardButton(text='Сам у меня спроси', callback_data='yes_3')
    itemp5_yes = ty.InlineKeyboardButton(text='Попозже', callback_data='yes_4')
    markup_inline.add(itemp1_yes, itemp2_no, itemp3_yes, itemp4_yes, itemp5_yes)
    bot_one.send_message(message.chat.id,'Хотите задать вопрос?', reply_markup = markup_inline)
#разобраться с переходом по кнопкам
@bot_one.callback_query_handler(func=lambda call: True)
def callback_inline(call, message):
    try:
        if call.message:
            if call.data == 'yes_1':
                markup_inline = ty.InlineKeyboardMarkup(row_width=2)
                temp1_yes = ty.InlineKeyboardButton(text='Овен', callback_data='yes1')
                temp2_no = ty.InlineKeyboardButton(text='Телец', callback_data='yes2')
                temp3_yes = ty.InlineKeyboardButton(text='Певец', callback_data='yes3')
                temp4_yes = ty.InlineKeyboardButton(text='Мудрец', callback_data='yes4')
                markup_inline.add(temp1_yes, temp2_no, temp3_yes, temp4_yes)
                #markup.add(item1, item2)
                bot_one.send_message(message.chat.id, 'Кто ты по гороскопу?', reply_markup=markup_inline)
                #bot_one.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'no_1':
                bot_one.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot_one.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)
            # show alert
            bot_one.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
    except Exception as e:
        print(repr(e))
#кнопка баланса, и по идее проверка баланса привязать(доделать)
@bot_one.message_handler(commands=['go'])
def send_go(message):
    bot_one.send_message(message.chat.id,
                         '''Приветики.
                         ''',
                         reply_markup=keyboyard())


@bot_one.message_handler(content_types=['text'])
def send_text(message):
    chat_id = message.chat.id
    if message.text == 'Баланс':
        text = 'Ваш баланс\n\n'
    bot_one.send_message(message.chat.id, text, parse_mode='html', reply_markup=keyboyard())

def keyboyard():
    mark =ty.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    botn1 = ty.KeyboardButton('Баланс')
    mark.add(botn1)
    return mark
bot_one.polling(none_stop=True)

