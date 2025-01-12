from random import choice

simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ''

ladno = int(input('Какой длинны будет пароль? '))

while ladno < 4:
    print('Пароль короче 4 символов!')
    ladno = int(input('Какой длинны будет пароль? '))

for i in range(ladno):
    password += choice(simvol)

print(f'Ваш пароль: {password}')