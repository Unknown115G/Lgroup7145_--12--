import telebot
import random
from telebot.types import ReactionTypeEmoji

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7762408720:AAGC2H7nNBFRs7sT8Vs0KAGMzJzu-DZdDz4")


@bot.message_handler(commands=['moments'])
def send_img(message):
    with open('image/Ладно.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open(f'image_s/mem{str(random.randint(1, 4))}.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Список команд:\n1. /help - Помощь по командам\n2. /start - Приветствие\n3. /hello - Привет\n4. /bye - Пока\n5. /moments - Моменты из VotV\n6. /mem - Рандомный мем")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)


bot.polling()