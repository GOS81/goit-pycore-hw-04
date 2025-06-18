# Завдання 1

# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

import re
from pathlib import Path

def total_salary(path):
    with open(path, "r", encoding="utf-8") as file:
        i = 0
        total = 0
        while True:
            line = file.readline()
            salary = re.search(r"\d+", line)
            if not line:
                break
            salary = int(salary.group())
            total = total + salary
            i += 1
        average = total // i
    return total, average

file_name = Path("salary.txt")
if file_name.exists():
    total, average = total_salary(file_name)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else: 
    print("file not found")