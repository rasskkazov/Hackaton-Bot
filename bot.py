import telebot
import config
import os
import gspread
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

sa = gspread.service_account(filename="hackaton-380713-5636952f4080.json")
sh = sa.open("Spisok_Abiturientov")
wks = sh.worksheet("Sheet1")
next = str(len(wks.col_values(1))+1)
place = "A"+next+":G"+next

hello_message="Добро пожаловать в официальный чат-бот Санкт-Петербургского государственного архитектурно-строительного университета! \nПриемная комиссия СПбГАСУ https://vk.com/spbgasu_priemnaia.\nВ 2022 году нашему университету исполнилось 190 лет. Его история тесно связана с историей архитектуры и градостроительства нашей страны и особенно Петербурга. \nБолее подробная информация на сайте: www.spbgasu.ru \nБудем признательны вам за активность, вопросы, предложения и пожелания!"
contacts="Россия, 190005, Московский пр., д. 29 \nПН-ЧТ        09:00 – 18:00\nПТ               09:00 – 17:00\nПерерыв  13:00 – 14:00 \n\n+7 (812) 316-20-26, \n+7 (812) 316-11-23, \n+7 (812) 575-94-53 (целевой прием)\n\nПочта: prc@spbgasu.ru\nVK: vk.com/spbgasu_priemnaia\nYouTube: https://rutube.ru/channel/25387641/\nTelegram: t.me/spbgasupriemnaia"
bakalavriat="07.03.01 Архитектура https://www.spbgasu.ru/applicants/areas-of-training/arkhitektura/\n08.03.01 Строительство https://www.spbgasu.ru/applicants/areas-of-training/arkhitektura/\n09.03.02 Информационные системы и технологии  \n\n Еще: https://www.spbgasu.ru/applicants/areas-of-training/?tab=0&search=&faculty= "
magistratura="07.04.01 Архитектура https://www.spbgasu.ru/applicants/areas-of-training/arkhitektura-m/ \n07.04.01 Строительство https://www.spbgasu.ru/applicants/areas-of-training/arkhitektura-m/ \n09.04.02 Информационные системы и технологии https://www.spbgasu.ru/applicants/areas-of-training/informatsionnye-sistemy-i-tekhnologii-m/ \n\n Еще: https://www.spbgasu.ru/applicants/areas-of-training/?tab=1&search=&faculty="
aspirantura="2.1.12 Архитектура зданий и сооружений. Творческие концепции архитектурной деятельности https://www.spbgasu.ru/applicants/areas-of-training/arkhitektura-zdaniy-i-sooruzheniy-tvorcheskie-kontseptsii-arkhitekturnoy-deyatelnosti/ \n2.1.7 Технология и организация строительства https://www.spbgasu.ru/applicants/areas-of-training/tekhnologiya-organizatsii-stroitelstva/\n1.2.2 Математическое моделирование, численные методы и комплексы программ https://www.spbgasu.ru/applicants/areas-of-training/matematicheskoe-modelirovanie-chislennye-metody-i-kompleksy-programm/ \n\nЕще: https://www.spbgasu.ru/applicants/areas-of-training/?tab=2&search=&faculty="


class Abiturient:
    def __init__(self):
        self.forma = ""
        self.osnova = ""
        self.naprav = ""
        self.name = ""
        self.surname = ""
        self.otchestvo = ""
        self.passport_photo_id = 0
        self.attestat_photo_id = 0
        self.phone = ""


class Napravlenie:
    def __init__(self, ochn, zaoc, budg, plat, nomer, nazvanie, budg_ege, price, plat_ege):
        self.ochn = ochn
        self.zaoc = zaoc
        self.budg = budg
        self.plat = plat
        self.nomer = nomer
        self.nazvanie = nazvanie
        self.budg_ege = budg_ege
        self.price = price
        self.plat_ege = plat_ege

abiturient = Abiturient()

#   оч   заоч бюдж платн номер     название бал_б стоимос бал_плат
napr1 = Napravlenie(True,True,True,True,"21.03.02","Землеустройство И Кадастры","167","70000","118")
napr2 = Napravlenie(True,True,True,True,"21.03.02","Строительство","203","80000","118")
napr3 = Napravlenie(True,True,True,True,"08.03.01","Технология транспортных процессов","161","70000","118")
napr4 = Napravlenie(True,True,True,True,"23.03.01","Эксплуатация транспортно-технологических машин и комплексов","135","256000","118")
napr5 = Napravlenie(True,False,False,True,"40.03.01","Юриспруденция","0","80000","120")
napr6 = Napravlenie(True,False,True,True,"40.03.01","Экономика","269","80000","114")
napr7 = Napravlenie(True,False,True,True,"13.03.01","Теплоэнергетика и теплотехника","149","221700","118")
napr8 = Napravlenie(True,False,True,True,"13.03.02","Техносферная безопасность","149","221700","118")


napr_list = [napr1, napr2, napr3, napr4, napr5,napr6,napr7,napr8]
cur_napr_list = napr_list


@bot.message_handler(commands=['start'])
def welcome(message):
    global cur_napr_list
    cur_napr_list = [napr1, napr2, napr3, napr4, napr5]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Чат с человеком")
    item2 = types.KeyboardButton("Подать документы")
    item3 = types.KeyboardButton("Информация для поступающих")
    item4=types.KeyboardButton("Контакты приемной комиссии")
    markup.add(item1, item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, hello_message, reply_markup=markup)
    # создать клавиутуру

@bot.message_handler(content_types=['text'])
def choose_welcome(message):
    if message.text == "Чат с человеком":
        bot.send_message(message.chat.id, "Чат с работником приёмной комиссии: @bogdan_bogdan2")
    if message.text == "Подать документы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Очная")
        item2 = types.KeyboardButton("Заочная")
        item3 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберите форму обучения: ", reply_markup=markup)
        bot.register_next_step_handler(message, choose_osnova)

    if message.text == "Информация для поступающих":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Очное/заочное обучение")
        item2 = types.KeyboardButton("Общежитие")
        item3 = types.KeyboardButton("Стипендия")
        item4 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1)
        markup.add(item2, item3)
        markup.add(item4)
        bot.send_message(message.chat.id, "О чем хотите узнать? ", reply_markup=markup)
        bot.register_next_step_handler(message, information_for_abiturient)

    if message.text == "Контакты приемной комиссии":
        markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, contacts, reply_markup=markup)
        bot.register_next_step_handler(message, information_for_abiturient)


def information_for_abiturient(message):
    if message.text == "Очное/заочное обучение":
        about_education(message)
    if message.text == "Общежитие":
        about_dormitory(message)
    if message.text == "Стипендия":
        about_scholarship(message)
    if message.text == "Вернуться в меню":
        message.text = ""
        welcome(message)
        return

def about_scholarship(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Вернуться в меню")
    markup.add(item)
    bot.send_message(message.chat.id, "https://old.spbgasu.ru/Studentam/Socialnaya_pomoshh/", reply_markup=markup)
    bot.register_next_step_handler(message, welcome)

def about_education(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Бакалавриат, специалитет")
    item2 = types.KeyboardButton("Магистратура")
    item3 = types.KeyboardButton("Аспирантура")
    item4 = types.KeyboardButton("Вернуться в меню")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, "Какая уровень образования вас интересует?", reply_markup=markup)
    bot.register_next_step_handler(message, choose_education)

def choose_education(message):

    if message.text == "Вернуться в меню":
        message.text = ""
        welcome(message)
        return
    if message.text == "Бакалавриат, специалитет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1)
        bot.send_message(message.chat.id, bakalavriat, reply_markup=markup)
        bot.register_next_step_handler(message, welcome)

    if message.text == "Магистратура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1)
        bot.send_message(message.chat.id, magistratura, reply_markup=markup)
        bot.register_next_step_handler(message, welcome)

    if message.text == "Аспирантура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1)
        bot.send_message(message.chat.id, aspirantura, reply_markup=markup)
        bot.register_next_step_handler(message, welcome)

def about_dormitory(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("МСГ")
    item2 = types.KeyboardButton("Фонтанка")
    item3 = types.KeyboardButton("Вернуться в меню")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "https://www.spbgasu.ru/applicants/dormitories/", reply_markup=markup)
    bot.register_next_step_handler(message, choose_dorm)

def choose_dorm(message):

    if message.text == "Вернуться в меню":
        message.text=""
        welcome(message)
        return
    if message.text == "Фонтанка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1)
        bot.send_message(message.chat.id, "https://www.spbgasu.ru/sveden/grants/#camp", reply_markup=markup)
        bot.register_next_step_handler(message, welcome)

    if message.text == "МСГ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вернуться в меню")
        markup.add(item1)
        bot.send_message(message.chat.id, "https://msg-spb.ru/%d0%b0%d0%b1%d0%b8%d1%82%d1%83%d1%80%d0%b8%d0%b5%d0%bd%d1%82%d0%b0%d0%bc/", reply_markup=markup)
        bot.register_next_step_handler(message, welcome)


def choose_osnova(message):
    if message.text == "Вернуться в меню":
        message.text=""
        welcome(message)
        return
    if message.text == "Очная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Бюджетная")
        item2 = types.KeyboardButton("Платная")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Выберите основу обучения: ", reply_markup=markup)
        # оставить направления очников
        for el in cur_napr_list:
            if el.ochn == False:
                cur_napr_list.remove(el)
        abiturient.forma = "Очная"
        bot.register_next_step_handler(message, choose_forma)

    if message.text == "Заочная":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Бюджетная")
        item2 = types.KeyboardButton("Платная")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Выберите основу обучения: ", reply_markup=markup)
        # оставить напрвления заочников
        for el in cur_napr_list:
            if el.zaoc == False:
                cur_napr_list.remove(el)
        abiturient.forma = "Заочная"
        bot.register_next_step_handler(message, choose_forma)


def choose_forma(message):
    if message.text == "Бюджетная":
        # отсеять напрвления платников
        for el in cur_napr_list:
            if el.budg == False:
                cur_napr_list.remove(el)
        # вывести список оставшихся направлений
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for el in cur_napr_list:
            markup.add(types.KeyboardButton(el.nazvanie))
        abiturient.osnova = "Бюджетная"
        bot.send_message(message.chat.id, "Выберите направление обучения: ", reply_markup=markup)

        bot.register_next_step_handler(message, choose_napr)

    if message.text == "Платная":
        # отсеять напрвления бюджетников
        for el in cur_napr_list:
            if el.plat == False:
                cur_napr_list.remove(el)
        # вывести список оставшихся направлений
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for el in cur_napr_list:
            markup.add(types.KeyboardButton(el.nazvanie))
        abiturient.osnova = "Платная"
        bot.send_message(message.chat.id, "Выберите направление обучения: ", reply_markup=markup)
        bot.register_next_step_handler(message, choose_napr)


def choose_napr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад")
    markup.add(item1)
    abiturient.naprav = message.text
    bot.send_message(message.chat.id, "Введите фамилию: ", reply_markup=markup)
    bot.register_next_step_handler(message, enter_surname)


def enter_surname(message):
    if message.text == "Назад":
        welcome(message)
        return
    else:
        abiturient.surname = message.text
        bot.send_message(message.chat.id, "Введите имя: ")
        bot.register_next_step_handler(message, enter_name)


def enter_name(message):
    if message.text == "Назад":
        message.text = ""
        choose_napr(message)
        return
    else:
        abiturient.name = message.text
        bot.send_message(message.chat.id, "Введите отчество: ")
        bot.register_next_step_handler(message, enter_otch)
    # здесь картинка выводится и подписывается электронной подписью


def enter_otch(message):
    if message.text == "Назад":
        message.text = ""
        enter_surname(message)
        return
    else:
        abiturient.otchestvo = message.text
        bot.send_message(message.chat.id,
                         'Введите  "подтвердить", чтобы подписать согласие на обработку персональных данных (заявление заверится электронной подписью)')
        bot.send_message(message.chat.id, 'Я, нижеподписавшийся(-ая) ' + abiturient.surname + " " + abiturient.name + " " + \
                         abiturient.otchestvo + " даю согласие Федеральному государственному бюджетному образовательному учреждению высшего\
            образования «Санкт-Петербургский государственный архитектурно-строительный университет», 190005, Санкт-Петербург г.,\
            2-я Красноармейская ул., дом № 4, на обработку своих персональных данных с использованием автоматизированной информационной\
            системы Федерального государственного бюджетного образовательного учреждения высшего образования «Санкт-Петербургский\
            государственный архитектурно-строительный университет». Обработка персональных данных с использованием автоматизированной\
            информационной системы Федерального государственного бюджетного образо-вательноrо учреждения высшего образования «Санкт-Петербургский\
            государственный архитектурно-строительный университет» осуществляется с целью содействия субъектам персональных данных в осуществлении\
            учебной, научной, трудовой деятельности, обеспечения личной безопасности, учета результатов исполнения договорных обязательств, а также\
            наиболее полного исполнения университетом обязательств и компетенций в соответствии с Федеральным законом «Об образовании в Российской\
            Федерации». Перечень персональных данных для обработки, должностных лиц, имеющий доступ к ним, определяется\
            Положением о работе с персональными данными автоматизированной \
            информационной системы Федерального государственного бюджетного образовательного учреждения высшего\
            образования «Санкт-Петербургский государственный архитектурно-строительный университет» \n Согласие действует в течение 5 лет.")
        bot.register_next_step_handler(message, confirmation)


def confirmation(message):
    if message.text == "Назад":
        message.text = ""
        enter_name(message)
        return
    elif message.text == "подтвердить":
        bot.send_message(message.chat.id,
                         'Проверьте свои данные: ' + " " + abiturient.name + " " + abiturient.surname + " " + abiturient.otchestvo + " " + abiturient.naprav + " " + abiturient.forma + " " + abiturient.osnova)
        bot.send_message(message.chat.id, 'Прикрепите фото паспорта (jpg, png):')
        bot.register_next_step_handler(message, get_passport_photo)
    else:
        message.text = ""
        enter_otch(message)
        return
def get_passport_photo(message):
    try:
        if message.content_type == 'photo':
            abiturient.passport_photo_id = message.photo[-1].file_id
            passport_photo = bot.get_file(abiturient.passport_photo_id)
            filename, file_ext = os.path.splitext(passport_photo.file_path)
            downloaded_passport_photo = bot.download_file(passport_photo.file_path)
            src = 'passport_photos/' + abiturient.surname+abiturient.name+abiturient.otchestvo+"_passport_photo" + file_ext
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_passport_photo)
            bot.send_message(message.chat.id, 'Прикрепите фото аттестата (jpg, png):')
            bot.register_next_step_handler(message, get_attestat_photo)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Назад")
            markup.add(item1)
            bot.send_message(message.chat.id, "Это не фото, попробуйте отправить еще раз (jpg, png)", reply_markup=markup)
            bot.register_next_step_handler(message, get_passport_photo)
    except Exception as e:
        bot.reply_to(message, 'ooops')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_message(message.chat.id, "Это не фото, попробуйте отправить еще раз (jpg, png)", reply_markup=markup)
        bot.register_next_step_handler(message, get_passport_photo)

def get_attestat_photo(message):
    try:
        if message.content_type == 'photo':
            abiturient.attestat_photo_id = message.photo[-1].file_id
            attestat_photo = bot.get_file(abiturient.attestat_photo_id)
            filename, file_ext = os.path.splitext(attestat_photo.file_path)
            downloaded_attestat_photo = bot.download_file(attestat_photo.file_path)
            src = 'attestat_photos/' + abiturient.surname+abiturient.name+abiturient.otchestvo+"_attestat_photo" + file_ext
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_attestat_photo)
            bot.send_message(message.chat.id, 'оставьте свой телефон:')
            bot.register_next_step_handler(message, get_phone)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Назад")
            markup.add(item1)
            bot.send_message(message.chat.id, "Это не фото, попробуйте отправить еще раз (jpg, png)", reply_markup=markup)
            bot.register_next_step_handler(message, get_attestat_photo)

    except Exception as e:
        bot.reply_to(message, 'ooops')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_message(message.chat.id, "Это не фото, попробуйте отправить еще раз (jpg, png)", reply_markup=markup)
        bot.register_next_step_handler(message, get_attestat_photo)

def get_phone(message):
    abiturient.phone = message.text
    wks.append_row([abiturient.surname, abiturient.name, abiturient.otchestvo, abiturient.naprav, abiturient.forma,
                    abiturient.osnova, abiturient.phone], table_range=place)
    bot.send_message(message.chat.id,
                     'база с абитуриентами (не отправляется пользователю): https://docs.google.com/spreadsheets/d/1MygHAnHAFPemMFvFQHuQQkKLc6qExgnR0NbCkwvvpk4/edit#gid=0')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, 'фотографии паспортов, аттестатов и т.п. хранятся на локальном диске', reply_markup=markup)
    bot.register_next_step_handler(message, welcome)



#run
bot.polling(none_stop=True)
