#Журнал ошибок ввода
from connstants import LOG_FILE
from datetime import datetime

entries:list[str]=[]

def log_error(message:str) -> None:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"[{time}] {message}"
    entries.append(record)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(record + "\n")
    except OSError:
        pass

def get_entries() -> list[str]:
    return entries.copy()
def clear() -> None:
    entries.clear()
