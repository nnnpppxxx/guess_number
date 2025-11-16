from random import *
from time import *

def start():
    global usercislo
    if usercislo == cislo: #вдруг с первой попытки угадают)
        print(f"Вау. Это лучший результат, с первой попытки угадал. Мое число действительно было {cislo}")
        #11111111111111

    while not is_valid(usercislo) : #пока пользователь не введет корректное число - запрашиваем опять число
        usercislo = int(input('Введите правильное число от 1 до 100: '))


def is_valid(num): #функция для проверки числа (не больше ста и не меньше 0)
    if num > 100:
        print('Число больше ста.')
        return False
    elif num < 1:
        print('Число меньше одного.')
        return False
    else:
        return True
  

def check_num(usercislo): #сама функция через которую пользователь угадывает число
    global count_for_game
    global count_win
    while usercislo != cislo:
        count_for_game -= 1
        if usercislo > cislo:
            print('-----------------------------------------')
            print(f'Твое число больше чем мое, осталось {count_for_game} попыток.')
        elif usercislo < cislo:
            print('-----------------------------------------')
            print(f'Твое число меньше чем мое, осталось {count_for_game} попыток.')
        if count_for_game == 0:
            print('-----------------------------------------')
            print('Увы. Ты проиграл, не расстраивайся, в следующий раз повезет!')
            print('-----------------------------------------')
            break
        print('-----------------------------------------')
        usercislo = int(input('Введите новое число от 1 до 100: '))
        count_win += 1
    if usercislo == cislo:
        sleep(1)
        print('-----------------------------------------')
        print('Ты угадал, поздравляю!')
        print(f'Ты угадал с {count_win} попыток.')
        print('-----------------------------------------')
        print('Начинаем новую игру?')
        new = input('Да или нет?: ')
        print('-----------------------------------------')
        if new.lower() == 'да':
            new_game_with_100()
        else:
            print('Окей, пока!')
            print('Приходи еще.')

        

def new_game_with_100():
    global cislo
    global count_for_game
    global count_win
    global usercislo
    cislo = randint(1,100)
    usercislo = int(input('Отгадай число от 1 до 100: '))
    count_for_game = 10
    count_win = 1
    start()
    check_num(usercislo)






# -----------------------MAIN------------------------------------
print('-----------------------------------------')
print('Добро пожаловать в игру Guess The Number!')
print('-----------------------------------------')
sleep(2)
print('''Как играть:
1. Я загадал число от 1 до 100, твоя задача угадать за 10 попыток.
2. В конце ты сможешь начать новую игру! Стань лучше остальных!
3. Удачи! =)''')
print('-----------------------------------------')
sleep(4)
cislo = randint(1, 100)
usercislo = int(input('Отгадай число от 1 до 100: '))
count_for_game = 10
count_win = 1
start()
check_num(usercislo)  # если все супер то переходим к функции угадывания 

