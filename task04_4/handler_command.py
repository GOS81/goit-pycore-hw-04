
def add(name, phone, dict):
    if name != None and phone != None:
        dict.append(
                {"name": name.capitalize(),
                 "phone": phone
                }
            )
        print(f"Контакт {name} додано!")
        return dict
    else:
        print("Введіть коректно данні: ім'я та телефон")

def change(name, new_phone, dict):
    for contact in dict:
        if contact["name"] == name:
            contact["phone"] = new_phone
            print(f"Номер телефона контакта {name} змінено на {new_phone}")
            return dict
        print("Контакт не знайдено")

def show(name, dict):
    for contact in dict:
        if contact["name"] == name:
            print(contact["name"], contact["phone"])

def all(dict):
    print(dict)
