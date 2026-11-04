try:
    n=int(input('Введите n:'))
    i=0
    count=0
    a=1
    while i<n and a>0:
        a=float(input('Введите число:'))
        f=a>0
        count+=f
        i+=1
    print('Положительных чисел в начале:',count) 
except ValueError:
      print('ошибка! необходимо ввести целое число')
