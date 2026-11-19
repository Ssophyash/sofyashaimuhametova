import time
from collections import deque
from typing import List, Sequence
def check_window(window, n):
    """Проверка, что окно корректное"""
    if window < 1:
        raise ValueError("Окно должно быть>= 1")
    if window > n:
        raise ValueError("Окно не может быть больше чем ряд")

def simple_moving_average(data, window):
    """
    Расчет скользящей средней через бегущую сумму.
    """
    check_window(window, len(data))

    #считаем сумму первых элементов
    running = sum(data[:window])
    result = [running / window]
    
    #идем по ряду, вычитая ушедший элемент и прибавляя новый
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

#самостоятельное задание 1
def centered_moving_average(data, window):
    """
    Центрированное скользящее среднее
    окно должно быть нечетным, чтобы центр приходился ровно
    """
    if window % 2 == 0:
        raise ValueError("для центрированного MA окно должно быть нечетным")
    check_window(window, len(data))
    #берем обычную SMA
    sma = simple_moving_average(data, window)
    #сдвигаем результат, чтобы он был по центру нашего окна
    shift = (window - 1) // 2
    #none по краям, чтобы длина совпадала с исходным рядом
    result = [0.0]*shift + sma + [0.0]*shift
    return result

#самостоятельное задание 2
def exponential_moving_average(data, alpha):
    if not (0 <alpha<= 1):
        raise ValueError("alpha должна быть в диапазоне (0, 1]")
    if not data:
        raise ValueError("ряд пусто1: расчёт невозможен")
    #первое значение EMA равно первому значению ряда
    result = [float(data[0])]
    for i in range(1, len(data)):
        ema = alpha*data[i] + (1 - alpha) * result[-1]
        result.append(ema)
    return result

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:
    """SMA с использованием deque (двусторонней очереди)."""
    check_window(window, len(data))
    result = []
    d = deque()
    running_sum = 0.0
    
    for x in data:
        d.append(x)
        running_sum += x
        
        if len(d) > window:
            running_sum -= d.popleft()
            
        if len(d) == window:
            result.append(running_sum / window)
            
    return result

def benchmark_moving_average(data: Sequence[float], window: int, repeats: int = 1000) -> dict:
    """
    Замеряет среднее время выполнения SMA для реализаций на list и deque.
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах).
"""
    # Проверка корректности окна (выбросит ValueError при необходимости)
    check_window(window, len(data))
    
    # Замер для list-реализации (существующая simple_moving_average)
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average(data, window)
    t_list = (time.perf_counter() - t0) / repeats
    
    # Замер для deque-реализации
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average_deque(data, window)
    t_deque = (time.perf_counter() - t0) / repeats
    
    return {"list": t_list, "deque": t_deque}

#функция скользящей медианы
def moving_median(data: list, window: int) -> list:
    check_window(window, len(data))#проверяем окно
    result = []
    for i in range(len(data) - window + 1):    # идем по ряду окнами
        current_window = sorted(data[i : i + window]) #сортируем часть ряда
        k = len(current_window) // 2 #середина
        
        if len(current_window) % 2!=0: #если окно нечетное
            result.append(float(current_window[k])) #берем центральный элемент
        else:
            result.append((current_window[k - 1] + current_window[k]) / 2.0) #берем среднее 2ух центральных элементов
            
    return result