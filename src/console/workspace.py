import readline
from colorama import Style, Fore, init
from .tab import tabs_in_mod
import sys
from time import sleep
from .help import help
import sys, os
from console.banner import print_banner
from prettytable import PrettyTable
from engien.dork import Dork

class Interact():
    #intitle:"index of /" intext:".env"

    def __init__(self) -> None:
        self.mod = ['Work', 'Search', 'Insert']
        self.current_mod = self.mod[0]
        self.cmd_on_mod = []
        self.tab_in_mod = tabs_in_mod
        self.input = ""
        self.url_output = []
        self.console_running = f'{Style.BRIGHT}{Fore.BLUE}[-]{Fore.RESET}{Style.RESET_ALL}]'
        self.console_ok  = f'{Style.BRIGHT}{Fore.GREEN}[+]{Fore.RESET}{Style.RESET_ALL}]'
        self.console_error = f'{Style.BRIGHT}{Fore.RED}[!]{Fore.RESET}{Style.RESET_ALL}]'

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
    
    def option(self, option=None):
        table = PrettyTable()
        table.field_names = []
        if self.current_mod.lower() == "search":
            table.field_names = tabs_in_mod['option'][self.current_mod.lower()]["field_names"]
            for val in tabs_in_mod['option'][self.current_mod.lower()]["val"]:
                name = val[0]
                value = val[1]
                required = val[2]
                discription = val[3]
                table.add_row([name, value, required, discription])
            return table
        return table
        
    def save(self):
        pass

    def show(self, option=None):
        
        
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

            #les commande de ce mode sont (help, mode, ) Work
            if self.current_mod == self.mod[0]:
                #changer de mode
                if self.input.split(" ")[0] == "use":
                    if self.input.split(" ")[1].capitalize() in self.mod:
                        self.current_mod = self.input.split(" ")[1].strip(" ").capitalize()
           
            #les commande de ce mode sont (set, run, show) Search 
            elif self.current_mod == self.mod[1] :
                match self.input.split(" ")[0].lower():
                    case "set":
                        match self.input.split(" ")[1].lower():
                            case 'vul':
                                tabs_in_mod["option"]['search']['val'][0][1] = self.input.split(" ")[2]
                            case 'dork':
                                tabs_in_mod["option"]['search']['val'][1][1] = self.input.strip("set dork ")
                            case 'target':
                                tabs_in_mod["option"]['search']['val'][2][1] = self.input.split(" ")[2]
                            case "scop":
                                tabs_in_mod["option"]['search']['val'][3][1] = int(self.input.split(" ")[2])

                    case "run":
                        self.url_output = Dork(
                                            result=tabs_in_mod["option"]['search']['val'][3][1],
                                            dork=tabs_in_mod["option"]['search']['val'][1][1],
                                            target=tabs_in_mod["option"]['search']['val'][2][1],
                                            dtype=tabs_in_mod["option"]['search']['val'][0][1]
                                            ).google()
                        pass
                    case "option":
                        print(self.option())
                    
                    case "flush":
                        if self.url_output:  
                            self.url_output = []
                            print (self.console_running+" Flush Output")
                        else:
                            print (self.console_error+" Output alredy empty !")
                    case "save":
                        if self.url_output:
                            pass
                        else:
                            print(self.console_error+" Empty Output !")

            #les commande de ce mode sont (set, run, show, ) Insert
            elif self.current_mod == self.mod[2]:
                match self.input:
                    case "set":
                        pass
                    case "run":
                        pass

            if self.input.split(" ")[0] == "back":
                    self.current_mod = self.mod[0]

            if self.input.split(" ")[0] == "show":
                pass
            #quiter la console   
            elif self.input.strip(" ") == "exit":
                print("Goodbye !")
                #sleep(1)
                sys.exit()
