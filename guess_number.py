from random import *

def is_valid(num):
    if num > 100:
        print('Число больше ста.')
        return False
    elif num < 1:
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
if is_valid(usercislo):
    check_num(usercislo)
else:
    usercislo = int(input('Введите правильное число от 1 до 100: '))
    if is_valid(usercislo):
        check_num(usercislo)
