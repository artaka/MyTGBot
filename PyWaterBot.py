import pyowm
import telebot

#Инициализация программы
owm = pyowm.OWM('25a9b982ae11ef72a41921508940fc16', language='ru')
TOKEN = '1006566418:AAHJBy44Kv28u_epk9irXaD-FG_hMS9HtDw'
bot = telebot.TeleBot(TOKEN)

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

Water_Complete_Message = "Сейчас в Мозыре " + Global_Status + " и " + str(Middle_Temp) + " градусов по цельсию. " + comment


@bot.message_handler(content_types=['text'])
def send_mess(message):
    if message.text == "Погода":
        bot.reply_to(message, Water_Complete_Message + RecommClother)
        print("Сообщение номер " + str(message.message_id) + " отправлено")
        print("Сообщение пользователя: " + str(message.text))
    elif message.text == "Привет":
        bot.reply_to(message, "Добрый день хозяин.")
        bot.send_message(563631084, "Чем могу помочь?")
        print("Сообщение номер " + str(message.message_id) + " отправлено")
        print("Сообщение пользователя: " + str(message.text))
        

bot.polling( none_stop = True )
