import time
from random import randint


def game(igrok):
    print('Кубик бросает', igrok)
    time.sleep(2)
    n = randint(1, 6)
    print('Выпало:', n)
    return n