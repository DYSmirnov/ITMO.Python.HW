def result(player1, player2, score1, score2):
    if score1 > score2:
        print('Выиграл', player1)
    elif score1 < score2:
        print('Выиграл', player2)
    else:
        print('Ничья')