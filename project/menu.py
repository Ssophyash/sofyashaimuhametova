def show_menu() -> None:
    """Вывести меню режимов."""
    print("\n Меню:")
    print("  1 — круглое сечение")
    print("  2 — прямоугольное сечение")
    print("  3 — кольцевое сечение")
    print("  0 — выход")


def select_mode() -> int | None:
    
    while True:
        show_menu()
        choice=input('Введите тип сечения:')
        match choice:
            case "1":
                return 1
            case "2":
                return 2
            case "3":
                return 3
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. ")
def mode_name(mode:int)->str:
    match mode:
        case 1:
            return 'круглое сечение'
        case 2:
            return 'прямоугольное сечение'
        case 3:
            return 'кольцевое сечение'
        case _:
            return'ошибка. тип сечения не распознан'