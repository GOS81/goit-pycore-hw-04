import sys
from pathlib import Path
from print_folder import print_folder

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
        print("Приклад: python main.py picture")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Шлях {path} не існує.")
        sys.exit(1)

    print_folder(path)


if __name__ == "__main__":
    main()