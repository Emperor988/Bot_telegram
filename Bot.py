import telebot
import random
import config
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['/start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число 🎲")
    item2 = types.KeyboardButton("Как дела? 😊")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == 'Рандомное число 🎲':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))

        elif message.text == '/start':
            bot.send_message(message.chat.id,
                                     text="Приветик, я бот-бронировщик, но для тебя я просто Броня! 🥰 ❤ ")
            bot.send_message(message.chat.id,
                                     text="Сейчас я нахожусь в разработки потерпи немного 😔 ")


        elif message.text == 'Привет 😊':
            bot.send_message(message.chat.id,
                                     text="Приветик, я бот-бронировщик, но для тебя я просто Броня! 🥰 ❤ ")
            bot.send_message(message.chat.id,
                                     text="Сейчас я нахожусь в разработки потерпи немного 😔 ")

        elif message.text == 'Как дела? 😊':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, а ты как?',reply_markup=markup)

        elif message.text ==  message.text:
             # keyboard
             keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
             item1 = types.KeyboardButton("Привет 😊")
             item2 = types.KeyboardButton("Рандомное число 🎲")
             item3 = types.KeyboardButton("Как дела? 😊")
             item4 = types.KeyboardButton("А что ты умеешь? 🤔")

             keybord.add(item1, item2, item3, item4)

             bot.send_message(message.chat.id, '2', reply_markup=keybord)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')







@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Юхууу, это прекрасно 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Эх, надеюсь все наладится 😞')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отлично, а ты как?",
                                 reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

            # keyboard
            # keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # item1 = types.KeyboardButton("Привет 😊")
            # item2 = types.KeyboardButton("Рандомное число 🎲")
            # item3 = types.KeyboardButton("Как дела? 😊")
            # item4 = types.KeyboardButton("А что ты умеешь? 🤔")
            #
            # keybord.add(item1, item2, item3, item4)

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)
