import pyowm
import telebot
from datetime import datetime

#Инициализация программы
owm = pyowm.OWM('25a9b982ae11ef72a41921508940fc16', language='ru')
TOKEN = '1006566418:AAHJBy44Kv28u_epk9irXaD-FG_hMS9HtDw'
bot = telebot.TeleBot(TOKEN)
print("Python Water Bot V2.3.2 Успешно запущен. Создатель @artakagrand")

#Массивы одежды
clotherSet1ShclAutumn = [
    "Кросовки Nike",
    "Чёрный джемпер",
    "Синие школьные штаны",
    "Зимняя курта",
    "Шапка The North Face"
]

clotherSet2ShclWinter = [
    "Зимние кросовки",
    "Клетчатая рубашка",
    "Чёрные штаны школьные",
    "Зимняя куртка",
    "Шапка The North Face"
]

clotherSet3Summer = [
    "Кросовки Nike",
    "Футболка NY",
    "Шорты Tommy Hilfiger",
    "Носки Puma",
]

place = ('Мозырь')

Obs = owm.weather_at_place(place)

w = Obs.get_weather()

Global_Status = w.get_detailed_status()

Middle_Temp = w.get_temperature('celsius')["temp"]

if Global_Status != "":
    print("Подключение к Open Water Map: OK")
print("Подключение к Telegram Bot Api: OK")
print("Ниже будут отображаться активность бота.")

comment = ""
if Middle_Temp < 10:
    comment = "Пиздец холодно. Если надо съебать то одевайся как на север нахуй."
    RecommClother = "Советую одеть эту одежду: " + clotherSet1ShclAutumn[0] + ", " + clotherSet1ShclAutumn[1] + ", " + clotherSet1ShclAutumn[2] + ", " + clotherSet1ShclAutumn[3] + ", " + clotherSet1ShclAutumn[4] + "."

elif Middle_Temp < 0:
    comment = "Холодно пизда, не умри блять."
    RecommClother = "Советую одеть эту одежду: " + clotherSet2ShclWinter[0] + ", " + clotherSet2ShclWinter[1] + ", " + clotherSet2ShclWinter[2] + ", " + clotherSet2ShclWinter[3] + ", " + clotherSet2ShclWinter[4] + "."

elif Middle_Temp > 20:
    comment = "Намана, тёпленько."
    RecommClother = "Советую одеть эту одежду: " + clotherSet3Summer[0] + ", " + clotherSet3Summer[1] + ", " + clotherSet3Summer[2] + ", " + clotherSet3Summer[3] + "."




@bot.message_handler(content_types=['text'])
def send_mess(message):
    Global_Status = w.get_detailed_status()
    Middle_Temp = w.get_temperature('celsius')["temp"]
    isCommand = False

    Water_Complete_Message = "Сейчас в Мозыре " + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + ". Погода: " + str(Middle_Temp) + " по цельсию и " + Global_Status + ". " + comment

    #Для вывода всех сообщений в консоль
    if message.text == "Погода":
        isCommand = True
        bot.reply_to(message, Water_Complete_Message)
        bot.send_message(message.chat.id, RecommClother)
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение номер " + str(message.message_id) + " отправлено")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение пользователя " + message.chat.first_name + " " + message.chat.last_name + " :"  + str(message.text))

    elif message.text == "Привет":
        isCommand = True
        bot.reply_to(message, "Добрый день хозяин.")
        bot.send_message(message.chat.id, "Чем могу помочь?")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение номер " + str(message.message_id) + " отправлено")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение пользователя " + message.chat.first_name + " " + message.chat.last_name + " :"  + str(message.text))

    elif message.text.find('report') != -1:
        isCommand = True
        bot.send_message(message.chat.id, "Ваш репорт примет мой создатель и обязательно исправит ошибку! Уведомление и текст был отправлен моему создателю.")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение номер " + str(message.message_id) + " отправлено.")
        bot.send_message(563631084, "!!!АЛЯРМ!!! Пришёл репорт от " + message.chat.first_name + " " + message.chat.last_name + " Пожалуйста проверьте консоль.")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Пришёл репорт от пользователя " + message.chat.first_name + " " + message.chat.last_name + " с описанием: " + message.text)

    elif message.text == "Создатель":
        isCommand = True
        bot.send_message(message.chat.id,"Мой создатель это @artakagrand/@niggaartem (inst)")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение номер " + str(message.message_id) + " отправлено.")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " + "Сообщение пользователя " + message.chat.first_name + " " + message.chat.last_name + " :"  + str(message.text))
    elif message.text.find('Диме') != -1:
        isCommand = True
        bot.send_message(message.chat.id, "Сообщение отправлено Диме.")
        bot.send_message(675899665, "Мой создатель передаёт вам: " + message.text)
        bot.send_message(675899665, "Чтобы ответить введите команду Артёму [текст]")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение номер " + str(message.message_id) + " отправлено.")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " + "Сообщение пользователя " + message.chat.first_name + " " + message.chat.last_name + " :"  + str(message.text))
    elif message.text.find('Артёму') != -1:
        isCommand = True
        bot.send_message(message.chat.id, "Сообщение отправлено Артёму.")
        bot.send_message(563631084, "Дмитрий передаёт вам: " + message.text)
        bot.send_message(563631084, "Чтобы ответить введите команду Диме [текст]")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Сообщение номер " + str(message.message_id) + " отправлено.")
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " + "Сообщение пользователя " + message.chat.first_name + " " + message.chat.last_name + " :"  + str(message.text))
    elif isCommand == False:
        print("[" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")) + "] " +  "Пришло сообщение от  пользователя " + message.chat.first_name + " " + message.chat.last_name + ". Сожержимое: " + str(message.text))
        

bot.polling( none_stop = True )
