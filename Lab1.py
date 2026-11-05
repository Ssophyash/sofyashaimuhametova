import math

print("1 — круглое сечение")
print("2 — прямоугольное сечение")
print("3 — кольцевое сечение")


f = True
while f:
    try:
        choice = int(input("Введите тип сечения: "))
        if 1 <= choice <= 3:
            f = False
        else:
            print("Ошибка: введите 1, 2 или 3")
    except ValueError:
        print("Ошибка: введите целое число")

match choice:
    case 1:
        f = True
        while f:
            try:
                d = float(input("Введите диаметр в мм: "))
                if d > 0:
                    f = False
                else:
                    print("Ошибка: диаметр должен быть положительным")
            except ValueError:
                print("Ошибка: введите число")
        A = math.pi * (d / 1000) ** 2 / 4
        razmer = d
        tip = "круглое сечение"
    case 2:
        f = True
        while f:
            try:
                a = float(input("Введите ширину в мм: "))
                b = float(input("Введите длину в мм: "))
                if a > 0 and b > 0:
                    f = False
                else:
                    print("Ошибка: размеры должны быть положительными")
            except ValueError:
                print("Ошибка: введите числа")
        A = (a / 1000) * (b / 1000)
        razmer = min(a, b)
        tip = "прямоугольное сечение"
    case 3:
        f = True
        while f:
            try:
                D = float(input("Введите внешний диаметр в мм: "))
                d = float(input("Введите внутренний диаметр в мм: "))
                if D > 0 and d > 0 and D > d:
                    f = False
                else:
                    print("Ошибка: D и d должны быть положительными, а D > d.")
            except ValueError:
                print("Ошибка: введите числа")
        A = math.pi * ((D / 1000) ** 2 - (d / 1000) ** 2) / 4
        razmer = D
        tip = "кольцевое сечение"
f = True
while f:
    try:
        v = float(input("Введите скорость потока  в м/с: "))
        if 0.1 <= v <= 10:
            f = False
        else:
            print("Ошибка: скорость должна быть от 0,1 до 10 м/с.")
    except ValueError:
        print("Ошибка: введите число.")
Q = A * v * 3600
print('Площадь сечения:',A,'м^2')
print('Расход жидкости:',Q,'м^3/ч')

if razmer < 25:
    klass = "малое сечение"
elif razmer <= 200:
    klass = "нормальное сечение"
else:
    klass = "крупное сечение"

    print('класс сечения:',klass)

