from typing import Annotated
from connstants import D_SMALL_LIMIT, D_LARGE_LIMIT
from connstants import PI, MM_TO_M,SECONDS_IN_HOUR

def circular_area(
        d:Annotated[float,'диаметр круглого сечения,мм']
)-> float:
    """
    вычисляет площадь круглого сечения в квадратных метрах.

    Args:
        d:диаметр сечения в мм.
    Returns:
        Площадь круглого сечения в квадратных метрах.
    """
    d_m=d/MM_TO_M
    return PI*d_m**2/4 

def rectangular_area(
         a: Annotated[float,'ширина прямоугольного сечения,мм'],
         b: Annotated[float,'высота прямоугольного сечения,мм'] 
)-> float:
    """
    вычисляет площадь прямоугольного сечения в квадратных метрах.

    Args:
        a:ширина сечения,мм
        b:высота сечения,мм
    Returns:
        Площадь прямоугольного сечения в квадратных метрах.
    """
    return (a/MM_TO_M)*(b/MM_TO_M)

def annular_area(
        D:Annotated[float,'внешний диаметр кольцевого сечения,мм'],
        d:Annotated[float,'внутренний диаметр кольцевого сечения,мм']
)->float:
    """
    вычисляет площадь кольцевого сечения в квадратных метрах.

    Args:
        D:внешний диаметр кольцевого сечения,мм
        d:внутренний диаметр кольцевого сечения,мм
    Returns:
        Площадь кольцевого сечения в квадратных метрах.
    """
    D_m= D/MM_TO_M
    d_m= d/ MM_TO_M
    return PI*(D_m**2-d_m**2)/4

def calculate_flow(
        area:Annotated[float,'площадь сечения,м2'],
        speed:Annotated[float,'скорость потока,м/с']
)->float:
    """
    вычисляет расход жидкости в м2/ч.

    Args:
        area:площадь сечения,м2
        speed:скорость потока,м/с
    returns:
        расход жидкости в м2/ч.
    """
    return area*speed*SECONDS_IN_HOUR

def diametr_class(
        d:Annotated[float,'размер сечения,мм']
)->str:
    """
    Определяет класс сечения в мм

    Args:
        d:размер сечения,мм
    returns:
        класс сечения в мм
    """
    if d<D_SMALL_LIMIT:
        return 'малое сечение' 
    elif d<=D_LARGE_LIMIT:
        return'нормальное сечение'
    else:
        return'крупное сечение'
