from pathlib import Path
from colorama import Back, Cursor, Fore, Style

def print_folder(path: Path, backdown: str = ""):
    if path.is_dir():
        print(Fore.BLUE + backdown + path.name + "/" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + backdown + path.name + Style.RESET_ALL)
    

    if path.is_dir():
        for child in sorted(path.iterdir()):
            print_folder(child, backdown + "    ")
