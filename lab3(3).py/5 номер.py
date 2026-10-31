""" n=int(input('Количество чисел:'))
a=[]
for i in range(n):
    a.append(int(input('введите число:')))
maximum=max(a)
print('максимальный элемент:',maximum)
print('порядковый номер:',a.index(maximum)+1) """

n=int(input('Количество чисел:'))
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