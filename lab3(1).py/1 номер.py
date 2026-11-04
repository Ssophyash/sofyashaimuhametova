try:
        a=int(input('введите целое число а<=200:'))
        if a<=200:
            summa=0
            count=0
            for i in range(a,201):
                 summa+=i
                 count+=1
            srednee=summa/count
            print('среднее арифметическое:',srednee)
        else:
             print('ошибка!число должно быть не больше 200')
except ValueError:
      print('ошибка! необходимо ввести целое число')
