#Журнал ошибок ввода
from connstants import LOG_FILE #импортируем имя файла для логов из констант
from datetime import datetime 

entries:list[str]=[] #создаем пустой список куда сохраняются все ошибки

def log_error(message:str) -> None: #функция принимает текст ошибки и ничего не возвращает
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"[{time}] {message}" #формируем итоговую строку
    entries.append(record)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file: #открываем файл в режиме а с коидровкой utf-8
            file.write(record + "\n")#записываем строку в файл и добавляем символ переноса
    except OSError:
        pass

def get_entries() -> list[str]:#возвращает список всех ошибок
    return entries.copy()
def clear() -> None:
    entries.clear()
