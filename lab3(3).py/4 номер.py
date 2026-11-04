try:
    n=int(input('Количество чисел:'))
    if n>0:
        a=[]
        for i in range(n):
            a.append(int(input('введите число:')))
        maximum=max(a)
        print('максимальный элемент:',maximum)
        print('порядковый номер:',a.index(maximum)+1)
    else:
        print('Ошибка! количество чисел должно быть больше 0')
except ValueError:
    print('Ошибка! необходимо вводить целые числа')
