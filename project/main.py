from validation import input_number, input_speed
from menu import show_menu, select_mode, mode_name
from operations import circular_area, rectangular_area,annular_area,calculate_flow,diametr_class
def main() -> None:

    while True:
        show_menu()
        mode = select_mode()
        if mode is None:
            print("Работа завершена.")
            return
        match mode:
            case 1:
                d=input_number('диаметр,мм',0,float('inf'))
                area=circular_area(a)
                size=d
            case 2:
                a=input_number('сторона а',0,float('inf'))
                b=input_number('сторона b',0,float('inf'))
                area=rectangular_area(a,b)
                size=min(a,b)
            case 3:
                D=input_number('',0,float('inf'))
                d=input_number('',0,float('inf'))
                area=annular_area(D,d)
                size=D
        speed=input_speed()
        flow=calculate_flow(area,speed)

        print('\nТип:',mode_name(mode))
        print(f'Площадь:{area:.6f}')
        print(f'Расход:{flow:.2f}')
        print('Класс:',diametr_class(size))

if __name__ == "__main__":
    main()