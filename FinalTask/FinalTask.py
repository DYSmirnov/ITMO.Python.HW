
def factorial():
    number = int(input("Введите число для которого хотите вычислить факториал  "))
    f = 1
    i = 1
    if i < number:
        for j in range(number):
            f = f*i
            i+=1
    print(f)

factorial()