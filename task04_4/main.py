from parse_input import *
#from handler_command import *


def main():
    print("\nВітаємо в нашому боті")
    while True:
        user_command = input("Введіть команду >>> ").strip()
        parse_input(user_command)
        


if __name__ == "__main__":
    main()
