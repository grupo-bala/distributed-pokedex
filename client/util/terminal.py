import os

def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
