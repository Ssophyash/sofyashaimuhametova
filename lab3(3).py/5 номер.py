try:
    n=int(input('Количество чисел:'))
    if n>0:
        a=[]
        for i in range(n):
            a.append(int(input('введите число:')))

        b=[]
        for number in a:
            if number%2!=0:
                b.append(number)
        if len(b)==0:
            print('нечетных чисел нет')
        else:
            b_sort=sorted(b,reverse=True)
            print('нечетные числа по убыванию:',b_sort)
    else:
        print('Ошибка! количество чисел должно быть больше 0')
except ValueError:
    print('Ошибка! необходимо вводить целые числа')
