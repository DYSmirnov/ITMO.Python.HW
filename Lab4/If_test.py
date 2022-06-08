from random import randint
import time


igrok1 = input('Введите имя 1-го играющего: ')
igrok2 = input('Введите имя 2-го играющего: ')
game_count = int(input('Введите количество партий: '))
sum1 = 0
sum2 = 0

for i in range(game_count):
    print('Игра №', i+1)
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1,6)
    print('Выпало:', n1)
    sum1 = n1 + sum1


    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1,6)
    print('Выпало:', n2)
    sum2 = n2 + sum2

if sum1>sum2:
    print('Игрок 1 набрал', sum1, 'очков.')
    print('Игрок 2 набрал', sum2, 'очков.')
    print('Выиграл', igrok1)
elif sum1<sum2:
    print('Игрок 1 набрал', sum1, 'очков.')
    print('Игрок 2 набрал', sum2, 'очков.')
    print('Выиграл', igrok2)
else:
    print('Игрок 1 набрал', sum1, 'очков.')
    print('Игрок 2 набрал', sum2, 'очков.')
    print('Ничья')