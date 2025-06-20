# Завдання 2

# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:
# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

from pathlib import Path

def get_cats_info(path):
    cats = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                cat_id, name, age = line.strip().split(',')
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                })
            except:
                print("damaged file")                
    return cats


file_name = Path("cat.txt")
if file_name.exists():
    cat_dict = get_cats_info(file_name)
    print(cat_dict)
else:
    print("file not found")