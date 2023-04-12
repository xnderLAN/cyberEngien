import readline
from colorama import Style, Fore, init
from .tab import tabs_in_mod
import sys
from time import sleep
from .help import help
from db.action import insert
import sys, os
from console.banner import print_banner
from prettytable import PrettyTable

class Interact():
    #intitle:"index of /" intext:".env"

    def __init__(self) -> None:
        self.mod = ['Work', 'Search', 'Insert']
        self.current_mod = 'work'
        self.cmd_on_mod = []
        self.tab_in_mod = tabs_in_mod
        self.input = ""

    def _tab(self, text, state):
        options = self.cmd_on_mod
        matches = [option for option in options if option.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None
    
    def _tab_maker(self):
        if self.current_mod :
            self.cmd_on_mod = self.tab_in_mod['all_cmd']
            return
        
        self.cmd_on_mod = self.cmd.keys()
    
    #action command
    def set(self):
        pass
    def run(self):
        pass
    def show(self, option=None):
        table = PrettyTable()
        table.field_names = []
        if option == "vul":
            return
        return
        
    def save(self):
        pass


    def console(self):
        if sys.platform == "linux":
            os.system("clear")
        elif sys.platform == "win32" or sys.platform == "win64" :
            os.system("cls")

        print_banner()
        init()
        
        while True:
            self._tab_maker()
            readline.set_completer(self._tab)
            readline.parse_and_bind('tab: complete')
            readline.set_completer_delims(' ')
            self.input = input(f'[{Style.BRIGHT}{Fore.RED}{self.current_mod.capitalize()}{Fore.RESET}{Style.RESET_ALL}] Doks {Style.BRIGHT}{Fore.RED}>>{Fore.RESET}{Style.RESET_ALL} ')

            #les commande de ce mode sont (help, mode, )
            if self.current_mod == "Work":
                #changer de mode
                if self.input.split(" ")[0] == "mode":
                    if self.input.split(" ")[1].capitalize() in self.mod:
                        self.current_mod = self.input.split(" ")[1].strip(" ").capitalize()
           
            #les commande de ce mode sont (set, run, show)
            elif self.current_mod == "Search" :
                match self.input.split(" ")[0].lower():
                    case "set":
                        pass
                    case "run":
                        pass
                    case "show":
                        pass

            #les commande de ce mode sont (set, run, show, )
            elif self.current_mod == "Insert":
                match self.input:
                    case "set":
                        pass
                    case "run":
                        pass

            if self.input.split(" ")[0] == "back":
                    self.current_mod = self.mod[0]
            
            #quiter la console   
            elif self.input.strip(" ") == "exit":
                print("Goodbye !")
                #sleep(1)
                sys.exit()
