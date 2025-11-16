from random import *

def is_valid(num):
    if num > 100:
        print('Число больше ста.')
        return False
    elif num < 0:
        print('Число меньше нуля.')
        return False
    elif num == 0:
        print('Число равно ноль.')
        return False
    else:
        return True
  

cislo = randint(1, 100)
print('Добро пожаловать в игру угадайку!')
usercislo = int(input('Введите число от 1 до 100: '))

count = 1


if is_valid(usercislo):
    while usercislo != cislo:
        if usercislo > cislo:
            print('Твое число больше чем загаданное')
        else:
            print('Твое число меньше чем загаданное')
        usercislo = int(input('Введите число от 1 до 100: '))
        count += 1
else:
    usercislo = int(input('Введите новое число от 1 до 100: '))


if usercislo == cislo:
    print('Угадал!')
    print(f'Кол-во попыток: {count}')

            
        