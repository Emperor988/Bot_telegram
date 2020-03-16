import telebot
#import config
from telebot import types

bot = telebot.TeleBot('1076383664:AAH79kaWVgTDE4l3EQi68d7Kel3ZMIFHcW4')

gv_menu = 'X'  # Отбражение меню бота
menu_view = '' # Проверка выводилось ли меню или нет

gv_step_line = '' # Ветка бота
gv_step = 0       # Шаг бота

################### ЗАМЕНИТЬ ###########################
### Переменные для проверки выводился ли шаг или нет ###
########################################################
gv_step_1 = ''
gv_step_2 = ''
gv_step_3 = ''
gv_step_4 = ''
gv_step_5 = ''
gv_step_6 = ''
########################################################

# Выход из меню на первы шаг выбранной ветки
def go_step(arg):
    if arg == 'res':
        global gv_step_line
        gv_step_line = 'res'
        next_step(1)

# Переход на следующий шаг
def next_step(arg):
    global gv_step
    gv_step = arg

# Вывод подменю ближайших дат в ветке
def button_date(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("15.03.2020", callback_data='date')
    item2 = types.InlineKeyboardButton("16.03.2020", callback_data='date')
    item3 = types.InlineKeyboardButton("17.03.2020", callback_data='date')
    item4 = types.InlineKeyboardButton("18.03.2020", callback_data='date')
    item5 = types.InlineKeyboardButton("19.03.2020", callback_data='date')
    item6 = types.InlineKeyboardButton("21.03.2020", callback_data='date')
    item7 = types.InlineKeyboardButton("22.03.2020", callback_data='date')
    item8 = types.InlineKeyboardButton("23.03.2020", callback_data='date')
    item9 = types.InlineKeyboardButton("24.03.2020", callback_data='date')
    item10 = types.InlineKeyboardButton("25.03.2020", callback_data='date')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

    # Выводим на экран
    bot.send_message(chat_id, 'Вот ближайшие даты:', reply_markup=markup)

# Уходим обратно в меню
def exit_menu(chat_id):

    global gv_menu, menu_view, gv_step_line, gv_step, gv_step_1, gv_step_2, gv_step_3, gv_step_4, gv_step_5, gv_step_6

    gv_menu = 'X'
    menu_view = ''
    gv_step_line = ''
    gv_step = 0  #
    gv_step_1 = ''
    gv_step_2 = ''
    gv_step_3 = ''
    gv_step_4 = ''
    gv_step_5 = ''
    gv_step_6 = ''
    message_menu(chat_id)

#-------------------------------------------------------------#
#---------------------Перенести в класс-----------------------#
#-------------Методы выводящие сообщения на экран-------------#
#-------------------------------------------------------------#
def message_menu(chat_id):
    global menu_view

    # Приветсвенное сообщение
    bot.send_message(chat_id,
                     text="Приветик, я бот-бронировщик, но для тебя я просто Броня! 🥰 ❤ ")

    # Пункты меню
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Забронировать переговку!", )
    keybord.add(item1)
    bot.send_message(chat_id, 'Чем я могу тебе помочь?', reply_markup=keybord)

    # Ставим что меню уже запустилось и его не надо отображать снова
    menu_view = 'X'

def message_time(chat_id):
    global gv_step_3
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("10:00", callback_data='time')
    item2 = types.InlineKeyboardButton("10:30", callback_data='time')
    item3 = types.InlineKeyboardButton("11:00", callback_data='time')
    item4 = types.InlineKeyboardButton("11:30", callback_data='time')
    item5 = types.InlineKeyboardButton("12:00", callback_data='time')
    item6 = types.InlineKeyboardButton("12:30", callback_data='room')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(chat_id, 'Выберите время планирования:', reply_markup=markup)

    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Перейти в меню")
    keybord.add(item1)
    bot.send_message(chat_id, 'Либо введите свой вариант, формат ЧЧ:ММ', reply_markup=keybord)

    gv_step_3 = 'X'

def message_room(chat_id):
    global gv_step_2

    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Перейти в меню")
    keybord.add(item1)
    bot.send_message(chat_id, 'Отлично, идём дальше', reply_markup=keybord)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1", callback_data='room')
    item2 = types.InlineKeyboardButton("2", callback_data='room')
    item3 = types.InlineKeyboardButton("3", callback_data='room')
    item4 = types.InlineKeyboardButton("4", callback_data='room')
    item5 = types.InlineKeyboardButton("5", callback_data='room')
    item6 = types.InlineKeyboardButton("Вече", callback_data='room')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(chat_id, 'Теперь нужно выбрать переговорку:', reply_markup=markup)
    gv_step_2 = 'X'

def message_lasting(chat_id):
    global gv_step_4

    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("30 минут", callback_data='lasting')
    item2 = types.InlineKeyboardButton("1 час", callback_data='lasting')
    item3 = types.InlineKeyboardButton("1,5 часа", callback_data='lasting')
    markup.add(item1, item2, item3)
    bot.send_message(chat_id, 'Выберите продолжительность встречи:', reply_markup=markup)

    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Перейти в меню")
    keybord.add(item1)
    bot.send_message(chat_id, 'Либо введите свой вариант продолжительности, формат ЧЧ:ММ', reply_markup=keybord)
    gv_step_4 = 'X'

def message_name(chat_id):
    global gv_step_5

    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Перейти в меню")
    keybord.add(item1)
    bot.send_message(chat_id, 'Введите название встречи(до 40 символов):', reply_markup=keybord)
    gv_step_5 = 'X'


#-------------------------------------------------------------#
@bot.message_handler(content_types=['text'])
def lalala(message):
        # Основное меню
        if gv_menu == 'X':
            if menu_view == '':
                message_menu(message.chat.id)
            # Определение ветки по которой идём
            elif message.text == 'Забронировать переговку!':
                go_step('res')

        # Идём по ветке бронирования
        if gv_step_line == 'res':

            # --- ВЫБОР ДАТЫ
            if gv_step == 1:
                global gv_step_1

                # Проверяем выводился ли на экран этот шаг
                if gv_step_1 != 'X':
                    bot.send_message(message.chat.id,
                                    text="Выберите дату бронировани, либо напишите свою")
                    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Показать ближайшие даты")
                    item2 = types.KeyboardButton("Перейти в меню")
                    keybord.add(item1, item2)
                    bot.send_message(message.chat.id, 'Формат даты: ДД.ММ.ГГГГ', reply_markup=keybord)
                    gv_step_1 = 'X'
                    button_date(message.chat.id)

                # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
                else:
                    if message.text == 'Показать ещё дат':
                        button_date(message.chat.id)
                    elif message.text == 'Перейти в меню':
                        exit_menu(message.chat.id)
                    # else:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! НЕОБХОДИМО РЕАЛИЗОВАТЬ ПРОВЕРКУ ДАТЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        # bot.send_message(message.chat.id, 'Формат даты: ДД.ММ.ГГГГ')

            # --- ВЫБОР ПЕРЕГОВОРКИ
            if gv_step == 2:
                # Проверяем выводился ли на экран этот шаг
                if gv_step_2 != 'X':
                    message_room(message.chat.id)

                # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
                else:
                    if message.text == 'Перейти в меню':
                        exit_menu(message.chat.id)
                    else:
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! НЕОБХОДИМО РЕАЛИЗОВАТЬ ПРОВЕРКУ КОМНАТЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        global gv_room
                        gv_room = message.text
                        next_step(3)

            # --- ВЫБОР ВРЕМЯ
            if gv_step == 3:
                # Проверяем выводился ли на экран этот шаг
                if gv_step_3 != 'X':
                    message_time(message.chat.id)

                 # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
                else:
                    if message.text == 'Перейти в меню':
                        exit_menu(message.chat.id)

            # --- ВЫБОР ПРОДОЛЖИТЕЛЬНОСТИ
            if gv_step == 4:
                # Проверяем выводился ли на экран этот шаг
                if gv_step_4 != 'X':
                    message_lasting(message.chat.id)

                # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
                else:
                    if message.text == 'Перейти в меню':
                        exit_menu(message.chat.id)

            # --- НАЗВАНИЕ ВСТРЕЧИ
            if gv_step == 5:
                # Проверяем выводился ли на экран этот шаг
                if gv_step_5 != 'X':
                    message_name(message.chat.id)

                # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
                else:
                    if message.text == 'Перейти в меню':
                        exit_menu(message.chat.id)
                    else:
                        global gv_name
                        gv_name = message.text
                        next_step(6)

            # --- ПОДТВЕРЖДЕНИЕ
            if gv_step == 6:
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Подтвердить", callback_data='yes')
                item2 = types.InlineKeyboardButton("Отменить", callback_data='no')
                markup.add(item1, item2)
                # bot.send_message(message.chat.id, 'Дата: + ', reply_markup=markup)
                bot.send_message(message.chat.id, 'Дата: ' + gv_date +
                                                  ', переговорка: ' + gv_room +
                                                  ', время: ' + gv_time +
                                                  ', продолжительность: ' + gv_lasting +
                                                  ', название встречи: ' + gv_name
                                 , reply_markup=markup)



        # else:
        #     bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            global gv_step
            global gv_chat_id
            gv_step = 0

            if call.data == 'yes':
                 bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text="Переговорка забронированна!")
                 exit_menu(call.message.chat.id)

            elif call.data == 'no':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text="Вы отменили бронирование, попробуйте ещё раз!")
                exit_menu(call.message.chat.id)

            elif call.data == 'date':
                global gv_date
                gv_date = call.message.text
                next_step(2)
                message_room(call.message.chat.id)

            elif call.data == 'room':
                global gv_room
                gv_room = call.message.text
                next_step(3)
                message_time(call.message.chat.id)

            elif call.data == 'time':
                global gv_time
                gv_time = call.message.text
                next_step(4)
                message_lasting(call.message.chat.id)

            elif call.data == 'lasting':
                global gv_lasting
                gv_lasting = call.message.text
                next_step(5)
                message_name(call.message.chat.id)

            # if call.data == '1':
            #     bot.send_message(call.message.chat.id, 'Юхууу, это прекрасно 😊')
            # elif call.data == '2':
            #     bot.send_message(call.message.chat.id, 'Эх, надеюсь все наладится 😞')

            # # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отлично, а ты как?",
            #                      reply_markup=None)

            # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
            #                           text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
