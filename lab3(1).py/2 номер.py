n=int(input('Введите n:'))
i=0
count=0
f=True
while i<n and f:
    num=float(input('Введите число:'))
    f=num>0
    count+=f
    i+=1
print('Положительных чисел в начале:',count) 