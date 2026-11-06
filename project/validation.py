from logger import log_error
from connstants import V_MIN,V_MAX

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    if value<low:
        return False, f'Ошибка:число должно быть не меньше {low}'
    elif value>high:
        return False, f'Ошибка:число должно быть не больше {high}'
    else:
        return True,''

def input_number(prompt: str, low: float, high: float) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)

def input_choice()-> int:
    #номер типа сечения
    while True:
        raw=input('выберите тип сечения:(1,2,3):').strip()
        try:
            choice=int(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введите целое число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue
        if choice<1:
            msg='ошибка,номер должен бытб:1,2 или 3'
            print(msg)
            log_error(msg)
        elif choice>3:
            msg='ошибка,номер должен бытб:1,2 или 3'
            print(msg)
            log_error(msg)
        else:
            return choice


def input_diameter() -> float:
    return input_number(
        "Введите диаметр, мм : ",
        0,
        float('inf')
    )


def input_speed() -> float:
    return input_number(
        "Введите скорость потока м/с : ",
        V_MIN, V_MAX,
    )

def inner_diametr(outer_diametr:float)-> float:
    while True:
        diametr=input_number('введите внутренний диаметр,мм',
                             0,
                             outer_diametr
        )
        if diametr<outer_diametr:
            return diametr
        msg='ошибка,внутренний диамтер должен быть меньше внешнего'
        print(msg)
        log_error(msg)
