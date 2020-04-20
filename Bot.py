import telebot
import config
from telebot import types
from planer_api import Methods

bot = telebot.TeleBot(token=config.token_bot)

gv_menu = 'X'  # Отбражение меню бота
gv_branch_name_1 = 'Забронировать переговку!'  # Первая ветка
menu_view = ''  # Проверка выводилось ли меню или нет

gv_step_line = ''  # Ветка бота
gv_step = 0  # Шаг бота

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
    item1 = types.InlineKeyboardButton("2020-04-19", callback_data='date1')
    item2 = types.InlineKeyboardButton("2020-04-20", callback_data='date2')
    item3 = types.InlineKeyboardButton("2020-04-21", callback_data='date3')
    item4 = types.InlineKeyboardButton("2020-04-22", callback_data='date4')
    item5 = types.InlineKeyboardButton("2020-04-23", callback_data='date5')
    item6 = types.InlineKeyboardButton("2020-04-24", callback_data='date6')
    item7 = types.InlineKeyboardButton("2020-04-25", callback_data='date7')
    item8 = types.InlineKeyboardButton("2020-04-26", callback_data='date8')
    item9 = types.InlineKeyboardButton("2020-04-27", callback_data='date9')
    item10 = types.InlineKeyboardButton("2020-04-28", callback_data='date10')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

    # Выводим на экран
    bot.send_message(chat_id, 'Выберите дату бронирования 📆 '
                              'Вот ближайшие даты:', reply_markup=markup)


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


# -------------------------------------------------------------#
# ---------------------Перенести в класс-----------------------#
# -------------Методы выводящие сообщения на экран-------------#
# -------------------------------------------------------------#
def message_menu(chat_id):
    global menu_view

    # Приветсвенное сообщение
    bot.send_message(chat_id,
                     text="Приветик, я бот-бронировщик, но для тебя я просто Броня! 🥰 ❤ ")

    # Пункты меню
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(gv_branch_name_1, )
    keybord.add(item1)
    bot.send_message(chat_id, 'Чем я могу тебе помочь?', reply_markup=keybord)

    # Ставим что меню уже запустилось и его не надо отображать снова
    menu_view = 'X'


def message_time(chat_id):
    global gv_step_3
    global gt_item
    global gt_item2
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("8:00", callback_data='time1')
    item2 = types.InlineKeyboardButton("8:30", callback_data='time2')
    item3 = types.InlineKeyboardButton("9:00", callback_data='time3')
    item4 = types.InlineKeyboardButton("9:30", callback_data='time4')
    item5 = types.InlineKeyboardButton("10:00", callback_data='time5')
    item6 = types.InlineKeyboardButton("10:30", callback_data='time5')
    item7 = types.InlineKeyboardButton("11:00", callback_data='time6')
    item8 = types.InlineKeyboardButton("11:30", callback_data='time7')
    item9 = types.InlineKeyboardButton("12:00", callback_data='time8')
    item10 = types.InlineKeyboardButton("12:30", callback_data='time9')
    item11 = types.InlineKeyboardButton("13:00", callback_data='time10')
    item12 = types.InlineKeyboardButton("13:30", callback_data='time11')
    item13 = types.InlineKeyboardButton("14:00", callback_data='time12')
    item14 = types.InlineKeyboardButton("14:30", callback_data='time13')
    item15 = types.InlineKeyboardButton("15:00", callback_data='time14')
    item16 = types.InlineKeyboardButton("15:30", callback_data='time15')
    item17 = types.InlineKeyboardButton("16:00", callback_data='time16')
    item18 = types.InlineKeyboardButton("16:30", callback_data='time17')
    item19 = types.InlineKeyboardButton("17:00", callback_data='time18')
    item20 = types.InlineKeyboardButton("17:30", callback_data='time19')
    item21 = types.InlineKeyboardButton("18:00", callback_data='time20')

    gt_item = [item1, '08:00', '', ''],\
              [item2, '08:30', '', ''],\
              [item3, '09:00', '', ''],\
              [item4, '09:30', '', ''],\
              [item5, '10:00', '', ''],\
              [item6, '10:30', '', ''],\
              [item7, '11:00', '', ''],\
              [item8, '11:30', '', ''],\
              [item9, '12:00', '', ''],\
              [item10, '12:30', '', ''],\
              [item11, '13:00', '', ''],\
              [item12, '13:30', '', ''],\
              [item13, '14:00', '', ''],\
              [item14, '14:30', '', ''],\
              [item15, '15:00', '', ''],\
              [item16, '15:30', '', ''],\
              [item17, '16:00', '', ''],\
              [item18, '16:30', '', ''],\
              [item19, '17:00', '', ''],\
              [item20, '17:30', '', ''],\
              [item21, '18:00', '', '']

    # CHECK BLOCK TIME
    events = Methods().get_events_list(
                                        level='13',
                                        room=gv_room,
                                        tmin=gv_date + 'T00:00:00.149205Z',
                                        tmax=gv_date + 'T23:00:00.149205Z'
                                      )

    global lv_block_time
    global lv_i
    lv_i = 0
    lv_block_time = ''

    for event in events:
        lv_block_time = 'x'

        start = event['start'].get('dateTime', event['start'].get('date'))
        lv_full = start.split('T')
        lv_time = lv_full[1].split('+')
        lv_hours = lv_time[0].split(':')
        lv_h_min = lv_hours[0] + ':' + lv_hours[1]

        end = event['end'].get('dateTime', event['end'].get('date'))
        lv_full = end.split('T')
        lv_time = lv_full[1].split('+')
        lv_hours = lv_time[0].split(':')
        lv_h_max = lv_hours[0] + ':' + lv_hours[1]



        for i in range(len(gt_item)):
            if gt_item[i][1] == lv_h_min:
                gt_item[i][2] = 'X'

                for i in range(len(gt_item)):
                    if gt_item[i][1] == lv_h_max:
                        break
                    elif gt_item[i][3] != 'X':
                        gt_item[i][2] = 'X'

                    # else:
                    #     gt_item[i][2] = 'X'

            gt_item[i][3] = 'X'

        # if lv_i == 0:
        #     A = [0] * (len(events))
        #
        # A[lv_i] = [lv_h_min, lv_h_max]
        # lv_i = lv_i + 1

    # if lv_block_time == 'x':
    #     lv_ch = 666
    #     for x in range(len(gt_item)):
    #         for l in range(len(A)):
    #             if gt_item[x][1] == A[l][0]:
    #                 lv_add = 'X'
    #                 # gt_item[x].append('X')
    #                 break
    #             else:
    #                 if lv_ch != x:
    #                     lv_add = ''
    #                     # gt_item[x].append('')
    #                     lv_ch = x

            # if lv_add == 'X':
            #     gt_item[x].append('X')
            # else:
            #     gt_item[x].append('')

    if lv_block_time == 'x':
        for n in range(len(gt_item)):
          if gt_item[n][2] != 'X':
            markup.add(gt_item[n][0])
    else:
        for n in range(len(gt_item)):
            markup.add(gt_item[n][0])

    bot.send_message(chat_id, 'Выберите время планирования:', reply_markup=markup)

    # keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton(gv_branch_name_1)
    # keybord.add(item1)
    # bot.send_message(chat_id, 'Либо введите свой вариант, формат ЧЧ:ММ', reply_markup=keybord)

    gv_step_3 = 'X'


def message_room(chat_id):
    global gv_step_2

    # keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton(gv_branch_name_1)
    # keybord.add(item1)
    # bot.send_message(chat_id, 'Отлично, идём дальше', reply_markup=keybord)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1 - С качелями", callback_data='room1')
    item2 = types.InlineKeyboardButton("2 - Развлекательная", callback_data='room2')
    item3 = types.InlineKeyboardButton("3 - Зелёная", callback_data='room3')
    item4 = types.InlineKeyboardButton("4 - Красная", callback_data='room4')
    item5 = types.InlineKeyboardButton("5 - Серая", callback_data='room5')
    item6 = types.InlineKeyboardButton("Вече", callback_data='room6')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(chat_id, 'Теперь нужно выбрать переговорку:', reply_markup=markup)
    gv_step_2 = 'X'


def message_lasting(chat_id):
    global gv_step_4

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 мин.", callback_data='lasting1')
    item2 = types.InlineKeyboardButton("1 час", callback_data='lasting2')
    item3 = types.InlineKeyboardButton("1 час 30 мин", callback_data='lasting3')
    item4 = types.InlineKeyboardButton("2 часа", callback_data='lasting4')
    markup.add(item1, item2, item3, item4)
    bot.send_message(chat_id, 'Выберите продолжительность встречи:', reply_markup=markup)

    # keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton(gv_branch_name_1)
    # keybord.add(item1)
    # bot.send_message(chat_id, 'Либо введите свой вариант продолжительности, формат ЧЧ:ММ', reply_markup=keybord)
    gv_step_4 = 'X'


def message_name(chat_id):
    global gv_step_5

    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(gv_branch_name_1)
    keybord.add(item1)
    bot.send_message(chat_id, 'Введите название встречи(до 40 символов):', reply_markup=keybord)
    gv_step_5 = 'X'


# -------------------------------------------------------------#
def calc_lasting(lasting):
    global gv_time_end
    # Расчитываем интервал
    lv_time = gv_time.split(':')

    if '1 час' == lasting:
        lv_arg = lv_time[0]
        lv_time_end = int(lv_arg) + 1
        gv_time_end = str(lv_time_end) + ':' + str(lv_time[1]) + ':' + str(lv_time[2])

    elif '2 часа' in lasting:
        lv_arg = lv_time[0]
        lv_time_end = int(lv_arg) + 2
        gv_time_end = str(lv_time_end) + ':' + str(lv_time[1]) + ':' + str(lv_time[2])

    elif '1 час 30 мин' == lasting:
        lv_arg = lv_time[0]
        lv_time_h = int(lv_arg) + 1

        lv_arg = lv_time[1]
        lv_time_m = int(lv_arg) + 30

        if lv_time_m == 60:
            lv_time_m = '00'
            lv_arg = lv_time[0]
            lv_time_h = lv_time_h + 1

        gv_time_end = str(lv_time_h) + ':' + str(lv_time_m) + ':' + str(lv_time[2])

    elif '30 минут' in lasting:
        lv_time_h = lv_time[0]
        lv_arg = lv_time[1]
        lv_time_m = int(lv_arg) + 30

        if lv_time_m == 60:
            lv_time_m = '00'
            lv_arg = lv_time[0]
            lv_time_h = int(lv_arg) + 1

        gv_time_end = str(lv_time_h) + ':' + str(lv_time_m) + ':' + str(lv_time[2])
# -------------------------------------------------------------#


# -------------------------------------------------------------#
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
                # keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
                # item1 = types.KeyboardButton("Показать ближайшие даты")
                # item2 = types.KeyboardButton(gv_branch_name_1)
                # keybord.add(item1, item2)
                # bot.send_message(message.chat.id, 'Выберите дату бронирования 📆', reply_markup=keybord)
                gv_step_1 = 'X'
                button_date(message.chat.id)

            # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
            else:
                if message.text == 'Показать ещё дат':
                    button_date(message.chat.id)
                elif message.text == 'Забронировать переговку!':
                    exit_menu(message.chat.id)
                # else:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! НЕОБХОДИМО РЕАЛИЗОВАТЬ ПРОВЕРКУ ДАТЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # bot.send_message(message.chat.id, 'Формат даты: ДД.ММ.ГГГГ')

        # --- ВЫБОР ПЕРЕГОВОРКИ
        if gv_step == 2:
            # Проверяем выводился ли на экран этот шаг
            if gv_step_2 != 'X':
                message_room(message.chat.id)

            # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
            else:
                if message.text == gv_branch_name_1:
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
                if message.text == gv_branch_name_1:
                    exit_menu(message.chat.id)

        # --- ВЫБОР ПРОДОЛЖИТЕЛЬНОСТИ
        if gv_step == 4:
            # Проверяем выводился ли на экран этот шаг
            if gv_step_4 != 'X':
                message_lasting(message.chat.id)

            # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
            else:
                if message.text == gv_branch_name_1:
                    exit_menu(message.chat.id)

        # --- НАЗВАНИЕ ВСТРЕЧИ
        if gv_step == 5:
            # Проверяем выводился ли на экран этот шаг
            if gv_step_5 != 'X':
                message_name(message.chat.id)

            # Если шаг выводился на экран, то мы смотрим что было введено пользователем на этом шаге
            else:
                if message.text == gv_branch_name_1:
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
            # bot.send_message(message.chat.id, @bold это *жирный*, _косой_ и `код`.)
            bot.send_message(message.chat.id,  "Название встречи: " + gv_name + "\n"
                                               "Переговорка: " + gv_room + "\n"
                                               'Дата: ' + gv_date + "\n"                                                                                              
                                               "Начало встречи: " + gv_time + "\n"
                                               "Продолжительность: " + gv_lasting + "\n" 
                                               "Конец встречи: " + gv_time_end
                                            ,  reply_markup=markup)

            gv_usr = message.from_user.username

            print("Название встречи: " + gv_name + "\n"
                                               "Переговорка: " + gv_room + "//"
                                               'Дата: ' + gv_date + "//"                                                                                              
                                               "Начало встречи: " + gv_time + "//"
                                               "Продолжительность: " + gv_lasting + "//" 
                                               "Конец встречи: " + gv_time_end + "//"
                                            , gv_usr )
    # else:
    #     bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    lv_stop = ''
    try:
        if call.message:
            global gv_lasting, gv_chat_id, gv_step, gv_date, gv_room, gv_time, gv_time_end
            gv_step = 0

            if call.data == 'yes':
                gv_usr = call.message.from_user.username
                Methods().create_event(
                    summary=gv_name,
                    location="Work",
                    dateTime_time_start=gv_time,
                    dateTime_date_start=gv_date,
                    dateTime_time_end=gv_time_end,
                    dateTime_date_end=gv_date,
                    description='TG.'+ gv_usr,
                    # email='',
                    level='13',
                    room=gv_room
                    )
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text="Переговорка забронирована!")
                bot.send_message(call.message.chat.id, 'Вы подтвердили бронирование.')
                exit_menu(call.message.chat.id)

            elif call.data == 'no':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text="Вы отменили бронирование, попробуйте ещё раз!")
                bot.send_message(call.message.chat.id, 'Вы отменили бронирование.')
                exit_menu(call.message.chat.id)

            # elif call.data == 'date':
            elif 'date' in call.data:
                # Достаём данные нажатой кнопочки подменю
                for i in range(len(call.message.json['reply_markup']['inline_keyboard'])):
                    for j in range(2):
                        if call.data == call.message.json['reply_markup']['inline_keyboard'][i][j]['callback_data']:
                            gv_date = call.message.json['reply_markup']['inline_keyboard'][i][j]['text']
                            lv_stop = 'X'
                            break
                    if lv_stop == 'X':
                        break

                next_step(2)
                bot.send_message(call.message.chat.id, 'Дата ' + gv_date + ' выбрана')
                message_room(call.message.chat.id)

            elif 'room' in call.data:
                # Достаём данные нажатой кнопочки подменю
                for i in range(len(call.message.json['reply_markup']['inline_keyboard'])):
                    for j in range(2):
                        if call.data == call.message.json['reply_markup']['inline_keyboard'][i][j]['callback_data']:
                            gv_room = call.message.json['reply_markup']['inline_keyboard'][i][j]['text']
                            lv_stop = 'X'
                            break
                    if lv_stop == 'X':
                        break
                next_step(3)
                bot.send_message(call.message.chat.id, 'Переговорка ' + gv_room + ' выбрана')
                message_time(call.message.chat.id)

            elif 'time' in call.data:
                # Достаём данные нажатой кнопочки подменю
                for i in range(len(call.message.json['reply_markup']['inline_keyboard'])):
                    for j in range(1):
                        if call.data == call.message.json['reply_markup']['inline_keyboard'][i][j]['callback_data']:
                            gv_time = call.message.json['reply_markup']['inline_keyboard'][i][j]['text']
                            gv_time=gv_time+':00'
                            lv_stop = 'X'
                            break
                    if lv_stop == 'X':
                        break
                next_step(4)
                bot.send_message(call.message.chat.id, 'Время с ' + gv_time + ' выбрано')
                message_lasting(call.message.chat.id)

            elif 'lasting' in call.data:
                # Достаём данные нажатой кнопочки подменю
                for i in range(len(call.message.json['reply_markup']['inline_keyboard'])):
                    for j in range(2):
                        if call.data == call.message.json['reply_markup']['inline_keyboard'][i][j]['callback_data']:
                            gv_lasting = call.message.json['reply_markup']['inline_keyboard'][i][j]['text']
                            lv_stop = 'X'
                            break
                    if lv_stop == 'X':
                        break

                calc_lasting(gv_lasting)
                next_step(5)
                bot.send_message(call.message.chat.id, 'Продолжительность ' + gv_lasting + ' выбрана')
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
