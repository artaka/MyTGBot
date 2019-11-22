import pyowm
import telebot

#Инициализация программы
owm = pyowm.OWM('25a9b982ae11ef72a41921508940fc16', language='ru')
TOKEN = '1006566418:AAHJBy44Kv28u_epk9irXaD-FG_hMS9HtDw'
bot = telebot.TeleBot(TOKEN)

#Массивы одежды
clotherSet1Shcl[
    "Кросовки Nike",
    "Чёрный джемпер",
    "Синие школьные штаны",
    "Зимняя курта",
    "Шапка The North Face"
]

clotherSet2Shcl[
    "Зимние кросовки",
    "Клетчатая рубашка",
    "Чёрные штаны школьные",
    "Зимняя куртка",
    "Шапка The North Face"
]

place = ('Мозырь')

Obs = owm.weather_at_place(place)

w = Obs.get_weather()

Global_Status = w.get_detailed_status()

Middle_Temp = w.get_temperature('celsius')["temp"]


comment = ""
if Middle_Temp < 10:
    comment = "Пиздец холодно. Если надо съебать то одевайся как на север нахуй."

elif Middle_Temp < 0:
    comment = "Холодно пизда, не умри блять."

elif Middle_Temp > 20:
    comment = "Намана, тёпленько."

Water_Complete_Message = "Сейчас в Мозыре " + Global_Status + " и " + str(Middle_Temp) + " градусов по цельсию. " + comment


@bot.message_handler(content_types=['text'])
def send_mess(message):
    if message.text == "Погода":
        bot.reply_to(message, Water_Complete_Message)
        print("Сообщение номер " + str(message.message_id) + " отправлено")
        print("Сообщение пользователя: " + str(message.text))
    elif message.text == "Привет":
        bot.reply_to(message, "Добрый день хозяин.")
        bot.send_message(563631084, "Чем могу помочь?")
        print("Сообщение номер " + str(message.message_id) + " отправлено")
        print("Сообщение пользователя: " + str(message.text))
        

bot.polling( none_stop = True )
