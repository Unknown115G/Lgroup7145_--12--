import telebot
import random
import time
from telebot.types import ReactionTypeEmoji, InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot("7753034089:AAEXzHMR6qhDrBgY13ZpiOOH-YdEgBJHrN8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для решения экологических проблем.")

def generate_keys():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Как 1', callback_data='1'),
                InlineKeyboardButton('Как 2', callback_data='2'))
    return keyboard

@bot.message_handler(commands=['priroda'])
def send_c(message):
    bot.send_message(message.chat.id, 'Как же помочь природе?', reply_markup=generate_keys())

@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == '1':
        bot.answer_callback_query(call.id, 'Никак 1', show_alert=True)
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Никак 2')