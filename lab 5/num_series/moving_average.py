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
