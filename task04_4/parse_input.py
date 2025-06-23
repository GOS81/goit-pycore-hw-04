from handler_command import add, change, show, all

contact_dictionary = []

def parse_input(input_command):
    cmd, *arg = input_command.split()
    cmd = cmd.lower()
    contact_name = arg[0].capitalize() if len(arg) > 0 else None
    contact_phone = arg[1] if len(arg) > 1 else None
    if cmd == "hello":
        print("Чим я можу вам допомогти?")

    elif cmd == "close" or cmd == "exit":
        print("Ви залишаєте додаток! \nГарного дня!")
        return exit()

    elif cmd == "add":
        add(contact_name, contact_phone, contact_dictionary)

    elif cmd == "change":
        change(contact_name, contact_phone, contact_dictionary)

    elif cmd == "show":
        show(contact_name, contact_dictionary)
    
    elif cmd == "all":
        all(contact_dictionary)

    else:
        print("Команда не знайдена! Спробуйте ще раз.")

    return contact_dictionary