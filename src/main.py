import db
from engien.dork import Dork
from colorama import Fore, Style, init
import readline


def banner():
    init()
    b= [
    ' ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███  ▓█████  ███▄    █   ▄████ ▓█████  ██▓ ███▄    █ ',
    '▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▓█   ▀  ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██▒ ██ ▀█   █ ',
    '▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██▒▓██  ▀█ ██▒',
    '▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ░██░▓██▒  ▐▌██▒',
    '▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒░▒████▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██░▒██░   ▓██░',
    '░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░▓  ░ ▒░   ▒ ▒ ',
    '░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░ ▒ ░░ ░░   ░ ▒░',
    '░       ▒ ▒ ░░   ░    ░    ░     ░░   ░    ░      ░   ░ ░ ░ ░   ░    ░    ▒ ░   ░   ░ ░ ',
    '░ ░     ░ ░      ░         ░  ░   ░        ░  ░         ░       ░    ░  ░ ░           ░ ',
    '░       ░ ░           ░                                                                     ',
    ]

    print()

    R = 148
    G = 0
    B = 211

    for i in b :

        red_code = f"\x1b[38;2;{R};{G};{B}m"
        print(red_code + i)

        R -= 10
        B -= 10
    
    print(Style.RESET_ALL)

class Interact():
    #intitle:"index of /" intext:".env"

    def __init__(self) -> None:
        pass

    def completer(self, text, state):
        options = ['commande1', 'commande2', 'commande3', 'flop', 'help'] # Remplacez cela par une liste de vos propres options de complétion
        matches = [option for option in options if option.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None
    def console(self):
        readline.set_completer(self.completer)
        readline.parse_and_bind('tab: complete')

        while True:
            commande = input('[NOD] Dork >> ')
            # traitez la commande ici...


if __name__ == "__main__":
    banner()
    Interact().console()