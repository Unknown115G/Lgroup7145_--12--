from flask import Flask
import random
from random import choice

app = Flask(__name__)

facts = [
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов",
    "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы",
    "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением"
]

@app.route("/")
def fact():
    return f'<p>Случайный факт про тех. зависимость!\n<a href="/random_fact">--- Загляни сюда ---</a></p><p>Генератор паролей\n<a href="/password">--- Генератор паролей ---</a></p>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts)}</p>'

@app.route("/password")
def password():
    simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ''

    for i in range(8):
        password += choice(simvol)

    return f'Ваш пароль: {password}'

app.run(debug=True)
