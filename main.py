import telebot
import constants
import kb
import menu
import chatID
import nameCategory
import reply
import re
import dj_database_url
import psycopg2

DATABASELINK = "postgres://jaffbnzlsirado:7439114eb04736d874c0a60ef1a437f66e934d269c11eab062351ee57f5e955f@ec2-174-129-254-250.compute-1.amazonaws.com:5432/d6gacovvq3jc2n"


db_info = dj_database_url.config(default=DATABASELINK)
connection = psycopg2.connect(database=db_info.get('d6gacovvq3jc2n'),
    user=db_info.get('jaffbnzlsirado'),
    password=db_info.get('7439114eb04736d874c0a60ef1a437f66e934d269c11eab062351ee57f5e955f'),
    host=db_info.get('ec2-174-129-254-250.compute-1.amazonaws.com'),
    port=db_info.get('5432'))
cursor = connection.cursor()

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    cursor.execute('CREATE TABLE public.variables (id integer NOT NULL,start boolean NOT NULL,kb1 boolean NOT NULL,kb2 boolean NOT NULL,kb3 boolean NOT NULL,kb4 boolean NOT NULL,kb4_2 boolean NOT NULL,kb111 boolean NOT NULL,kb112 boolean NOT NULL,kb121 boolean NOT NULL,kb122 boolean NOT NULL,kb13 boolean NOT NULL,kb13_1 boolean NOT NULL,kb211 boolean NOT NULL,kb212 boolean NOT NULL,kb221 boolean NOT NULL,kb222 boolean NOT NULL,number_auto character varying NOT NULL,tel character varying NOT NULL,condition character varying NOT NULL);')
    menu.start = True
    menu.kb1 = False
    menu.kb2 = False
    menu.kb3 = False
    menu.kb4 = False
    menu.kb111 = False
    menu.kb112 = False
    menu.kb121 = False
    menu.kb122 = False
    menu.kb13 = False
    menu.kb211 = False
    menu.kb212 = False
    menu.kb221 = False
    menu.kb222 = False
    menu.tel = ""
    menu.number_auto = ""
    menu.condition = ""
    bot.send_message(message.chat.id, reply.start, reply_markup=kb.keyboard0)


@bot.message_handler(commands=['Назад'])
def back_message(message):
    if menu.start == True:
        menu.kb1 = False
        menu.kb2 = False
        menu.kb3 = False
        menu.kb4 = False
        menu.kb111 = False
        menu.kb112 = False
        menu.kb121 = False
        menu.kb122 = False
        menu.kb13 = False
        menu.kb13_1 = False
        menu.kb211 = False
        menu.kb212 = False
        menu.kb221 = False
        menu.kb222 = False
        menu.tel = ""
        menu.number_auto = ""
        menu.condition = ""
        bot.send_message(message.chat.id, reply.start, reply_markup=kb.keyboard0)
    elif menu.kb111 == True or menu.kb112 == True or menu.kb121 == True or menu.kb122 == True or menu.kb13 == True:
        menu.start = True
        menu.kb1 = True
        menu.kb111 = False
        menu.kb112 = False
        menu.kb121 = False
        menu.kb122 = False
        menu.kb13 = False
        bot.send_message(message.chat.id, reply.R1, reply_markup=kb.keyboard1)
    elif menu.kb13_1 == True:
        menu.kb13 = True
        menu.kb13_1 = False
        bot.send_message(message.chat.id, reply.R1_1, reply_markup=kb.keyboardL)
    elif menu.kb211 == True or menu.kb212 == True or menu.kb221 == True or menu.kb222 == True:
        menu.start = True
        menu.kb211 = False
        menu.kb212 = False
        menu.kb221 = False
        menu.kb222 = False
        bot.send_message(message.chat.id, reply.r02, reply_markup=kb.keyboard2)
    elif menu.kb4 == True:
        menu.kb4 = False
        menu.start = True
        bot.send_message(message.chat.id, reply.start, reply_markup=kb.keyboard4)
    elif menu.kb4_2 == True:
         menu.kb4_2 = False
         menu.kb4 = True
         bot.send_message(message.chat.id, reply.r42, reply_markup=kb.keyboard4)
    else:
        bot.send_message(message.chat.id, "Error")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    # keyboard0 основное меню
    if message.text == nameCategory.c01:
        bot.send_message(message.chat.id, reply.r01, reply_markup=kb.keyboard1)
    elif message.text == nameCategory.c02:
        bot.send_message(message.chat.id, reply.r02, reply_markup=kb.keyboard2)
    elif message.text == nameCategory.c03:
        bot.send_message(message.chat.id, reply.r03, reply_markup=kb.keyboard3)
    elif message.text == nameCategory.c04:
        bot.send_message(message.chat.id, reply.r04, reply_markup=kb.keyboard4)

# keyboard1 Состояние авто
    elif message.text == nameCategory.c111:
        menu.kb1 = True
        menu.kb111 = True
        menu.kb112 = False
        menu.kb121 = False
        menu.kb122 = False
        menu.kb13 = False
        bot.send_message(message.chat.id, reply.R1)
    elif message.text == nameCategory.c112:
        menu.kb1 = True
        menu.kb112 = True
        menu.kb111 = False
        menu.kb121 = False
        menu.kb122 = False
        menu.kb13 = False
        bot.send_message(message.chat.id, reply.R1)
    elif message.text == nameCategory.c121:
        menu.kb1 = True
        menu.kb121 = True
        menu.kb111 = False
        menu.kb112 = False
        menu.kb122 = False
        menu.kb13 = False
        bot.send_message(message.chat.id, reply.R1)
    elif message.text == nameCategory.c122:
        menu.kb1 = True
        menu.kb122 = True
        menu.kb111 = False
        menu.kb112 = False
        menu.kb121 = False
        menu.kb13 = False
        bot.send_message(message.chat.id, reply.R1)
    elif message.text == nameCategory.c13:
        menu.kb1 = True
        menu.kb13 = True
        menu.kb111 = False
        menu.kb112 = False
        menu.kb121 = False
        menu.kb122 = False
        bot.send_message(message.chat.id, reply.R1)

# keyboard1 обработчик номера телефона
    elif menu.kb1 == True:
          if re.match(r'[7-8]{1}[0-9]{10}', message.text) or re.match(r'[+]{1}[7-8]{1}[0-9]{10}', message.text):
            menu.kb1 = False
            menu.start = False
            menu.tel = message.text
            bot.send_message(message.chat.id, reply.R1_1, reply_markup=kb.keyboardL)
          else:
            bot.send_message(message.chat.id, reply.tel)
# Номер авто
# 1 - 4
    elif menu.kb111 == True:
        if re.match(r'[a-zA-Zа-яА-Я]{1}[0-9]{3}[a-zA-Zа-яА-Я]{2}', message.text):
            menu.kb111 = False
            menu.start = True
            menu.number_auto = message.text
            bot.send_message(message.chat.id, reply.r1send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, (nameCategory.c111 + " автомобиля c номером " + menu.number_auto + " (Тел: " + menu.tel + ")"))
            menu.number_auto = ""
            menu.tel = ""
        else:
            bot.send_message(message.chat.id, reply.number)

    elif menu.kb112 == True:
        if re.match(r'[a-zA-Zа-яА-Я]{1}[0-9]{3}[a-zA-Zа-яА-Я]{2}', message.text):
            menu.kb112 = False
            menu.start = True
            menu.number_auto = message.text
            bot.send_message(message.chat.id, reply.r1send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, (nameCategory.c112+ " автомобиля c номером " + menu.number_auto + " (Тел: " + menu.tel + ")"))
            menu.number_auto = ""
            menu.tel = ""
        else:
            bot.send_message(message.chat.id, reply.number)

    elif menu.kb121 == True:
        if re.match(r'[a-zA-Zа-яА-Я]{1}[0-9]{3}[a-zA-Zа-яА-Я]{2}', message.text):
            menu.kb121 = False
            menu.start = True
            menu.number_auto = message.text
            bot.send_message(message.chat.id, reply.r1send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, (nameCategory.c121 + " у автомобиля c номером " + menu.number_auto + " (Тел: " + menu.tel + ")"))
            menu.number_auto = ""
            menu.tel = ""
        else:
            bot.send_message(message.chat.id, reply.number)

    elif menu.kb122 == True:
        if re.match(r'[a-zA-Zа-яА-Я]{1}[0-9]{3}[a-zA-Zа-яА-Я]{2}', message.text):
            menu.kb122 = False
            menu.start = True
            menu.number_auto = message.text
            bot.send_message(message.chat.id, reply.r1send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, (nameCategory.c122 + " в автомобиле c номером " + menu.number_auto + " (Тел: " + menu.tel + ")"))
            menu.number_auto = ""
            menu.tel = ""
        else:
            bot.send_message(message.chat.id, reply.number)

# 5 Описание проблемы
    elif menu.kb13 == True:
        if re.match(r'[a-zA-Zа-яА-Я]{1}[0-9]{3}[a-zA-Zа-яА-Я]{2}', message.text):
            menu.kb13 = False
            menu.kb13_1 = True
            menu.number_auto = message.text
            bot.send_message(message.chat.id, reply.r13)
        else:
            bot.send_message(message.chat.id, reply.number)

    elif menu.kb13_1 == True:
        menu.kb13_1 = False
        menu.start = True
        menu.condition = message.text
        bot.send_message(message.chat.id, reply.r1send, reply_markup=kb.keyboard1)
        bot.send_message(chatID.Dmitriy, ("Автомобиль c номером " + menu.number_auto + " (Тел: " + menu.tel + ") /// " + menu.condition))
        menu.tel = ""
        menu.number_auto = ""
        menu.condition = ""

# keyboard2 Нужна помощь, проблема
    elif message.text == nameCategory.c211:
        menu.kb211 = True
        menu.start = False
        bot.send_message(message.chat.id, reply.R2, reply_markup=kb.keyboardL)
    elif message.text == nameCategory.c212:
        menu.kb212 = True
        menu.start = False
        bot.send_message(message.chat.id, reply.R2, reply_markup=kb.keyboardL)
    elif message.text == nameCategory.c221:
        menu.kb221 = True
        menu.start = False
        bot.send_message(message.chat.id, reply.R2, reply_markup=kb.keyboardL)
    elif message.text == nameCategory.c222:
        menu.kb222 = True
        menu.start = False
        bot.send_message(message.chat.id, reply.R2, reply_markup=kb.keyboardL)
    elif message.text == nameCategory.c23:
        bot.send_message(message.chat.id, "+79991255722",reply_markup=kb.keyboard0 )
#keyboard2 обработчик номера телефона
    elif menu.kb211 == True:
        if re.match(r'[7-8]{1}[0-9]{10}', message.text) or re.match(r'[+]{1}[7-8]{1}[0-9]{10}', message.text):
            menu.kb211 = False
            menu.start = True
            bot.send_message(message.chat.id, reply.r2send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, nameCategory.c211 + " " + message.text)
        else:
            bot.send_message(message.chat.id, reply.tel)
    elif menu.kb212 == True:
        if re.match(r'[7-8]{1}[0-9]{10}', message.text) or re.match(r'[+]{1}[7-8]{1}[0-9]{10}', message.text):
            menu.kb212 = False
            menu.start = True
            bot.send_message(message.chat.id, reply.r2send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, nameCategory.c212 + " " + message.text)
        else:
            bot.send_message(message.chat.id, reply.tel)
    elif menu.kb221 == True:
        if re.match(r'[7-8]{1}[0-9]{10}', message.text) or re.match(r'[+]{1}[7-8]{1}[0-9]{10}', message.text):
            menu.kb221 = False
            menu.start = True
            bot.send_message(message.chat.id, reply.r2send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, nameCategory.c221 + " " + message.text)
        else:
            bot.send_message(message.chat.id, reply.tel)
    elif menu.kb222 == True:
        if re.match(r'[7-8]{1}[0-9]{10}', message.text) or re.match(r'[+]{1}[7-8]{1}[0-9]{10}', message.text):
            menu.kb222 = False
            menu.start = True
            bot.send_message(message.chat.id, reply.r2send, reply_markup=kb.keyboard0)
            bot.send_message(chatID.Dmitriy, nameCategory.c222 + " " + message.text)
        else:
            bot.send_message(message.chat.id, reply.tel)
 # keyboard3 FAQ
    elif message.text == nameCategory.c31:
        bot.send_message(message.chat.id, reply.r31)
    elif message.text == nameCategory.c32:
        bot.send_message(message.chat.id, reply.r32)
    elif message.text == nameCategory.c33:
        bot.send_message(message.chat.id, reply.r33)
    elif message.text == nameCategory.c34:
        bot.send_message(message.chat.id, reply.r34)
    elif message.text == nameCategory.c35:
        bot.send_message(message.chat.id, reply.r35)
    elif message.text == nameCategory.c36:
        bot.send_message(message.chat.id, reply.r36)
    elif message.text == nameCategory.c37:
        bot.send_message(message.chat.id, reply.r37)
    elif message.text == nameCategory.c38:
        bot.send_message(message.chat.id, reply.r38)
    elif message.text == nameCategory.c39:
        bot.send_message(message.chat.id, reply.r39)
    elif message.text == nameCategory.c310:
        bot.send_message(message.chat.id, reply.r310)
    elif message.text == nameCategory.c311:
        bot.send_message(message.chat.id, reply.r311)
    elif message.text == nameCategory.c312:
        bot.send_message(message.chat.id, reply.r312)
    elif message.text == nameCategory.c313:
        bot.send_message(message.chat.id, reply.r313)
    elif message.text == nameCategory.c314:
        bot.send_message(message.chat.id, reply.r314)
    elif message.text == nameCategory.c315:
        bot.send_message(message.chat.id, reply.r315)
    elif message.text == nameCategory.c316:
        bot.send_message(message.chat.id, reply.r316)

# keyboard 4 Заправка автомобиля
    elif message.text == nameCategory.c41:
        menu.kb4 = False
        bot.send_message(message.chat.id, reply.r41)
    elif message.text == nameCategory.c42:
        menu.kb4 = True
        bot.send_message(message.chat.id, reply.r42)
    elif menu.kb4 == True:
        if re.match(r'[7-8]{1}[0-9]{10}', message.text) or re.match(r'[+]{1}[7-8]{1}[0-9]{10}', message.text):
            menu.kb4 = False
            menu.start = False
            menu.kb4_2 = True
            menu.tel = message.text
            bot.send_message(message.chat.id, reply.r4_2, reply_markup=kb.keyboardL)
        else:
            bot.send_message(message.chat.id, reply.tel)
    elif menu.kb4_2 == True:
        bot.send_message(message.chat.id, reply.r4_2)

# ELSE
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, используйте меню для доступа к моим функциям. Выберите интересующий вас пункт.')


@bot.message_handler(content_types=['photo', 'document'])
def handle_docs_audio(message):
    if menu.kb4_2 == True:
        menu.kb4_2 = False
        menu.start = True
        bot.send_message(message.chat.id, reply.r4send, reply_markup=kb.keyboard4)
        bot.send_message(chatID.Dmitriy, menu.tel)
        bot.forward_message(chatID.Dmitriy, message.chat.id, message.message_id)
        menu.tel = ""


bot.polling(none_stop=True, interval=0)
