import time
from random import randint



def main():
    player1 = enter_name(1)
    player2 = enter_name(2)

    score1 = game(player1)
    score2 = game(player2)

    result(player1, player2, score1,score2)

def enter_name(number):
    player_name = input(f'Введите имя {number}-го играющего: ')
    print(number)
    return player_name

def game(igrok):
    print('Кубик бросает', igrok)
    time.sleep(2)
    n = randint(1, 6)
    print('Выпало:', n)
    return n

def result(player1, player2, score1, score2):
    if score1 > score2:
        print('Выиграл', player1)
    elif score1 < score2:
        print('Выиграл', player2)
    else:
        print('Ничья')
main()