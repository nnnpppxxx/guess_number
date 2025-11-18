from random import randint
from time import sleep

def start(cislo_program, usercislo): #функция для старта игры и проверки первого введенного числа  
    while not is_valid(usercislo) : #пока пользователь не введет корректное число - запрашиваем опять число
        usercislo = input('Введите правильное число от 1 до 100: ')
    if int(usercislo) == cislo_program: #вдруг с первой попытки угадают)
        print(f"Вау. Это лучший результат, с первой попытки угадал. Мое число действительно было {cislo_program}!")
        return
    return int(usercislo)


def is_valid(usercislo):
    if not usercislo.isdigit(): #функция для проверки числа (не больше ста и не меньше 0)
        print('Это не число.')
        return False
    elif int(usercislo) > 100:
        print('Число больше ста.')
        return False
    elif int(usercislo) < 1:
        print('Число меньше одного.')
        return False
    else:
        return True
  

def check_num(usercislo):
    global count
    while usercislo != cislo:
        if usercislo > cislo:
            print('Твое число больше чем загаданное')
        else:
            print('Твое число меньше чем загаданное')
        usercislo = int(input('Введите число от 1 до 100: '))
        count += 1
        if usercislo == cislo:
            print('Угадал')
            print(f'Количество попыток: {count}')


cislo = randint(1, 100)
print('Добро пожаловать в игру угадайку!')
usercislo = int(input('Введите число от 1 до 100: '))
count = 0

while not is_valid(usercislo) :
    usercislo = int(input('Введите правильное число от 1 до 100: '))

check_num(usercislo)   
