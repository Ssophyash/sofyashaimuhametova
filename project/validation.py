from logger import log_error  #импортируем функцию логирования ошибок
from constants import V_MIN, V_MAX  #импортируем границы скорости

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:  #принимает число и границы, возвращает кортеж и текст ошибки
    if value < low:  #если значение меньше нижней границы
        return False, f'Ошибка: число должно быть не меньше {low}'  #возвращаем ложь и текст ошибки
    elif value > high:  #если больше верхней границы
        return False, f'Ошибка: число должно быть не больше {high}'  #возвращаемложь и текст
    else:  
        return True, ''  

def input_number(prompt: str, low: float, high: float) -> float:  #функция для безопасного ввода числа
    while True: 
        raw = input(prompt).strip()  #получаем ввод и убираем лишние пробелы по краям
        try:  
            value = float(raw)  #преобразуем строку в число с типом флоат
        except ValueError as e:  #если не получилось (напр,ввели буквы), то ошибка
            msg = str(e.args[0]) if e.args else str(e)  #достаем текст системной ошибки 
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"  #формируем понятное сообщение
            print(msg)  
            log_error(msg)  
            continue  

        ok, msg = validate_range(value, low, high)  #проверяем число на допустимый диапазон
        if ok: 
            return value  # если пройдено то возвращаем это число из функции 
        print(msg + " Повторите ввод.")  
        log_error(msg)  

def input_choice() -> int:  #ввод номера меню 
    while True:  
        raw = input('выберите тип сечения:(1,2,3):').strip()  
        try: 
            choice = int(raw)  
        except ValueError as e:  
            msg = str(e.args[0]) if e.args else str(e) 
            msg = f"Ошибка: введите целое число ('{raw}'). {msg}" 
            print(msg)  
            log_error(msg)  
            continue  
        
        if choice < 1:  
            msg = 'ошибка, номер должен быть: 1, 2 или 3'  
            print(msg)  
            log_error(msg)  
        elif choice > 3:  
            msg = 'ошибка, номер должен быть: 1, 2 или 3'  
            print(msg) 
            log_error(msg)  
        else:
            return choice 

def input_diameter() -> float:  #ввода диаметр
    return input_number(  
        "Введите диаметр, мм : ", 
        0,  
        float('inf')  #верхняя граница бесконечность float('inf'), тк ограничений сверху нет
    )

def input_speed() -> float:  #ввод скорости
    return input_number(  
        "Введите скорость потока м/с:",  
        V_MIN,V_MAX,  
    )

def inner_diameter(outer_diameter: float) -> float:  #проверяем что внутренний диаметр меньше внешнего
    while True:  
        diameter = input_number(  
            'введите внутренний диаметр,мм',  
            0,  
            outer_diameter  #верхняя граница не больше внешнего диаметра 
        )
        if diameter < outer_diameter:  
            return diameter
        msg = 'ошибка, внутренний диаметр должен быть меньше внешнего'  
        print(msg)  
        log_error(msg)  
