# #!/usr/bin/python
# ## -*- coding: utf-8 -*-
import telebot
import config 
import buttons
import os 
import requests
import threading


administrators = (842234154, ) 
users = {}
users_text = {}
users_text_2 = {}
my_poll = {} 

poll_1 = {} 
poll_2 = {} 
poll_3 = {} 
poll_4 = {} 
poll_5 = {} 
poll_6 = {} 
poll_7 = {} 
poll_8 = {} 
poll_9 = {} 
poll_10 = {} 
poll_11 = {} 
poll_12 = {} 
poll_13 = {} 
poll_14 = {} 
poll_15 = {} 

bot = telebot.TeleBot(config.TOKEN, threaded = True)

@bot.message_handler(commands = ['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 
        f'''
        Выбери, кого ты хочешь оценить? 👇
    ''', parse_mode = "Markdown", reply_markup = buttons.Main_menu())


@bot.message_handler(func=lambda message: message.text == 'Оценить подразделение 🏢')
def review_SP(message):
    bot.send_message(message.chat.id, 'Выберите подразделение:', reply_markup = buttons.review_SP())



@bot.message_handler(func=lambda message: message.text == 'Оценить сотрудника 🙎‍♂️')
def input_emploee(message):        
    bot.send_message(message.chat.id, 'Пожалуйста, введите ФИО сотрудника, которого Вы бы хотели оценить:')
    users[message.chat.id] = {}
    bot.register_next_step_handler(message, save_msg_text)
 
def save_msg_text(message):
    users[message.chat.id]['emploee'] = message.text
    bot.send_message(message.chat.id, f'Сохранить данные?', reply_markup = buttons.Save_Change())

def send_feedback_administrators(message):
    feedback = message.text
    user = users[message.chat.id]
    emploee = user['emploee']
    for admin_chat_id in administrators:
        bot.send_message(admin_chat_id, f'''Оценили сотрудника: {emploee}.
                         \nОбщая оценка "{user['review_Text']}" с отзывом: "{feedback}"''')
    bot.send_message(message.chat.id, 'Ваш отзыв успешно *сохранён*!', parse_mode = "Markdown") 


# @bot.message_handler(func=lambda message: message.text == 'Пройти опрос 📊')
# def pool_X(message):
#     bot.send_message(message.chat.id, '*Если необходимо отменить голос:*\n\t1. Кликните один раз по голосованию.'\
#             '\n\t2. В появившемся меню выберите "Отменить голос".\n\t3. Переголосуйте правильно.', parse_mode = "Markdown")
#     if my_poll == {}:
#         pool_X = bot.send_poll(message.chat.id, 
#             question = f'Обращаетесь ли Вы к ключевым компетенциям сотрудников при использвании 📞Телефонного справочника ТНЭ?',
#             options = ['Да', 'Нет'], is_anonymous = 0, allows_multiple_answers = 0)
#         my_poll['ls'] = [message.chat.id, pool_X.message_id] 
#         # print(my_poll) 
#     else: 
#         bot.forward_message(message.chat.id, my_poll['ls'][0], my_poll['ls'][1])

# @bot.message_handler(func=lambda message: message.text == 'Высказать своё мнение 🙋')
# def say_mind(message):
#     bot.send_message(message.chat.id, 'Пожалуйста, напишите Ваш отзыв о работе подразделений 🌟'
#         'Мы ценим любые комментарии, которые помогут нам улучшить работу.💥'
#         'Что Вам нравится? Что стоит скорректировать? Мы хотим знать все Ваши мысли и предложения🤔:')
#     users_text[message.chat.id] = {}
#     bot.register_next_step_handler(message, send_feedback_administrators_1)

# def send_feedback_administrators_1(message):
#     users_text[message.chat.id]['usertext'] = message.text
#     for admin_chat_id in administrators:
#         bot.send_message(admin_chat_id, f'{users_text}')
#     bot.send_message(message.chat.id, f'Ваши отзывы важны для нас. Спасибо за ваше участие! 🚀') #reply_markup = ls_keyboards()

# @bot.message_handler(func=lambda message: message.text == 'Предложить улучшение 📈')
# def add_offer(message):
#     bot.send_message(message.chat.id, 
#         'Пожалуйста, напишите Ваши предложения по улучшению работы подразделений или процесса📈'
#         '/nМы готовы рассмотреть любые идеи, которые могут повысить эффективность и качество работы:')
#     users_text[message.chat.id]= {}
#     bot.register_next_step_handler(message, send_feedback_administrators_1)

# def send_feedback_administrators_2(message):
#     users_text_1[message.chat.id]['usertext'] = message.text
#     for admin_chat_id in administrators:
#         bot.send_message(admin_chat_id, f'{users_text_1}')
#     bot.send_message(message.chat.id, 
#         f'Ваш вклад важен для нас. Спасибо за участие! 🚀')

# @bot.message_handler(func=lambda message: message.text == 'Посмотреть отчеты 📑')
# def sent_develop(message):
#     ls_img = {'1': 'Рейтинг клиентоцентричности структурных подзразделений общества', 
#               '2': 'Статистика в разрезе месяцев'}
#     for key, value in ls_img.items():
#         with open((os.path.abspath(f'images/{key}.jpg')), 'rb') as file:
#             bot.send_photo(message.chat.id, file.read(), caption = f'{value}')

# @bot.message_handler(func=lambda message: message.text == 'Написать разработчику ❓')
# def sent_develop(message):
#     bot.send_message(message.chat.id, 
#         'Мы будем рады услышать ваши идеи, комментарии или вопросы✅'
#         '\nВсе ваши отзывы помогут нам улучшить работу бота и сделать его еще удобнее🚀'
#         '\nКонтакт: @Mari_YakovlevM ')



# Обработчик встроенной клавиатуры
@bot.callback_query_handler(func = lambda msg: True)
def callback_Func(call):
    message = call.message
    text = call.data

    # ------------------------- раздел "Оценить подразделение" ----------------------------
    def pool_review_SP(arg_text, arg_poll_result):
        if arg_poll_result == {}:
            my_poll = bot.send_poll(message.chat.id, 
                question = f'Оцени {arg_text},отправь сообщение с цифрой',
                options = ['Отлично 😇', 'Нейтрально 😑', 'Плохо 😡'], is_anonymous = 1, allows_multiple_answers = 0)
            arg_poll_result['ls'] = [message.chat.id, my_poll.message_id] # добавляем данные в словарь
            # print(my_poll)
            # print(arg_poll_result)

            #для оценки подразделений
            def send_feedback_administrators_1(message):
                users_text[message.chat.id]['usertext'] = message.text
                for admin_chat_id in administrators:
                    bot.send_message(admin_chat_id, f'Сотрудник оставил отзыв подразделению {arg_text}: {message.text}')
                bot.send_message(message.chat.id, f'Ваши отзывы важны для нас. Спасибо за ваше участие! 🚀')

            bot.send_message(message.chat.id, 'После прохождения опроса ниже напишите, почему Вы поставили именно такую оценку🤔:')
            users_text[message.chat.id] = {}
            bot.register_next_step_handler(message, send_feedback_administrators_1)
        else: 
            bot.forward_message(message.chat.id, arg_poll_result['ls'][0], arg_poll_result['ls'][1])

    if 'ПЭО' in text:
        pool_review_SP(text, poll_1)
   
    if 'СИБ' in text:
        pool_review_SP(text, poll_2)

    if 'ОИ' in text: 
        pool_review_SP(text, poll_3)

    if 'ОСД РРЭ' in text:
        pool_review_SP(text, poll_4)
   
    if 'СПУФ' in text: 
        pool_review_SP(text, poll_5)

    if 'ОБ' in text: 
        pool_review_SP(text, poll_6)

    if 'ОУП' in text: 
        pool_review_SP(text, poll_7)

    if 'ОСД ОРЭ' in text: 
        pool_review_SP(text, poll_8)
       
    if 'СОПТ' in text: 
        pool_review_SP(text, poll_9)

    if 'ОД' in text: 
        pool_review_SP(text, poll_10)

    if 'ОАЗИ' in text: 
        pool_review_SP(text, poll_11)

    if 'СКОВ' in text: 
        pool_review_SP(text, poll_12)
       
    if 'ООПД' in text: 
        pool_review_SP(text, poll_13)

    if 'СЭМ' in text: 
        print(text)
        pool_review_SP(text, poll_14)

    if 'СППБОТ' in text: 
        pool_review_SP(text, poll_15)

    # ------------------------- раздел "Оценить сотрудника" ----------------------------
    if 'save_data' in call.data:
        message_id = call.message.message_id
        bot.answer_callback_query(call.id, text = "Данные сохранены")
        bot.delete_message(chat_id = call.message.chat.id, message_id = message_id)
        bot.send_message(call.message.chat.id, 
            f'Как Вы оцениваете работу сотрудника {users[call.message.chat.id]['emploee']}?', 
            parse_mode = "Markdown", reply_markup = buttons.review_Text())
        
    if 'change_data' in call.data:
        input_emploee(call.message)
    
    # варианты общей оценки сотрудника
    if 'Отлично' in call.data or 'Нейтрально' in call.data or 'Плохо' in call.data:
        print(f'Ваш текст {call.data}')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.message_id)
        users[call.message.chat.id]['review_Text'] = call.data
        print(users)
        bot.send_message(call.message.chat.id, 
            'Укажите, что Вам понравилось в его работе, и что, по вашему мнению, можно улучшить:')
        bot.register_next_step_handler(call.message, send_feedback_administrators)




# ------------------------------------------------------------------------------------
if __name__ == '__main__':
    def runBot():
        bot.polling(none_stop = True, interval = 0, timeout = 100)

    t1 = threading.Thread(target = runBot)
    t1.start()

