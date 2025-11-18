from random import randint
from time import sleep

def start(cislo_program, usercislo): #функция для старта игры и проверки первого введенного числа  
    if usercislo == cislo_program: #вдруг с первой попытки угадают)
        print(f"Вау. Это лучший результат, с первой попытки угадал. Мое число действительно было {cislo_program}!")
        return
    while not is_valid(usercislo) : #пока пользователь не введет корректное число - запрашиваем опять число
        usercislo = int(input('Введите правильное число от 1 до 100: '))
    return usercislo


def is_valid(usercislo): #функция для проверки числа (не больше ста и не меньше 0)
    if usercislo > 100:
        print('Число больше ста.')
        return False
    elif usercislo < 1:
        print('Число меньше одного.')
        return False
    elif not usercislo.isdigit():
        print('Это не число.')
        return False
    else:
        return True
  

def check_num(usercislo, cislo_program, count_for_game, count_win): #сама функция через которую пользователь угадывает число
    while usercislo != cislo_program:
        count_for_game -= 1
        if usercislo > cislo_program:
            print('-----------------------------------------')
            print(f'Твое число больше чем мое, осталось {count_for_game} попыток.')
        elif usercislo < cislo_program:
            print('-----------------------------------------')
            print(f'Твое число меньше чем мое, осталось {count_for_game} попыток.')
        if count_for_game == 0:
            print('-----------------------------------------')
            print('Увы. Ты проиграл, не расстраивайся, в следующий раз повезет!')
            print('-----------------------------------------')
            return
        print('-----------------------------------------')
        usercislo = int(input('Введите новое число от 1 до 100: '))
        while not is_valid(usercislo) : #пока пользователь не введет корректное число - запрашиваем опять число
            usercislo = int(input('Введите правильное число от 1 до 100: '))
        count_win += 1
    
    sleep(1)
    print('-----------------------------------------')
    print('Ты угадал, поздравляю!')
    print(f'Ты угадал с {count_win} попыток.')
    print('-----------------------------------------')
    return

        

def new_game_with_100():
    cislo_program = randint(1,100)
    usercislo = int(input('Отгадай число от 1 до 100: '))
    count_for_game = 10
    count_win = 1
    usercislo = start(cislo_program, usercislo)
    check_num(usercislo, cislo_program, count_for_game, count_win)









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


while True:
    new_game_with_100()  
    print('Начинаем новую игру?')  
    new = input('Да или нет?: ')
    print('-----------------------------------------')
    if new.lower() != 'да':
        print('Окей, пока!')
        print('Приходи еще.')
        break 


