import random
import statistics

def ex_2_3_4():
    lst = generate_list(100, amount=10)
    print("Список: ", lst)
    print("Сумма списка = ", sum(lst))
    print("Среднее значение списка = ", statistics.mean(lst))
    print("Медиана списка = ", statistics.median(lst))
    print("Стандартное отклонение списка = ", statistics.stdev(lst))



def generate_list( end_value, start_value = 1, amount = 1):
    lst = []
    if amount == 1:
        return random.randint(start_value, end_value)
    else:
        for i in range(amount):
            lst.append(random.randint(start_value, end_value))
        return lst

ex_2_3_4()