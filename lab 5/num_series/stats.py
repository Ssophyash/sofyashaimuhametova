import math
from typing import Dict, Sequence
def _ensure_not_empty(data: Sequence[float]) -> None:
 if not data:
    raise ValueError("Ряд пуст: расчёт статистики невозможен")
def mean(data: Sequence[float]) -> float:
    """Среднее арифметическое."""
    _ensure_not_empty(data)
    return sum(data) / len(data)
def median(data: Sequence[float]) -> float:
    """Медиана (устойчива к выбросам)."""
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0
def spread(data: Sequence[float]) -> float:
    """Размах ряда: max - min."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))
def summarize(data: Sequence[float]) -> Dict[str, float]:
    """Сводный отчёт: count, mean, median, spread, min, max."""
    _ensure_not_empty(data)
    return {
    "count": len(data),
    "mean": mean(data),
    "median": median(data),
    "spread": spread(data),
    "min": float(min(data)),
    "max": float(max(data)),
    }

def unique_count(data: list) -> int: # проверяем, что нам не передали пустой список
    _ensure_not_empty(data) 
    return len(set(data)) #set(data) убираем  дубликаты, и считаем, сколько осталось

def shannon_entropy(data: list) -> float:
    _ensure_not_empty(data)
    counts = count(data) #считаем сколько раз встречается каждое число 
    total = len(data) #общее количество чисел в ряду
    entropy = 0.0
    for count in counts.values():
        p = count / total #считаем долю этого числа в этом ряду
        entropy += p * math.log2(p)
    return -entropy
