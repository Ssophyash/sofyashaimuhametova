s=input('введите строку:')
if s!='':
    s=s.lower()
    s_new=s.replace('a','o').replace('а','о')
    count=s.count('a')+s.count('а')
    dlina=len(s)
    print('новая строка:',s_new)
    print('количество замен:',count)
    print('количество символов',dlina) 
else:
    print('Ошибка! строка не должна быть пустой')
