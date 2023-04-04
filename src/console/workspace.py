import readline
from colorama import Style, Fore, init
from .tab import tabs_in_mod
import sys
from time import sleep


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

    def console(self):
        
        init()
        
        while True:
            self._tab_maker()
            readline.set_completer(self._tab)
            readline.parse_and_bind('tab: complete')
            self.input = input(f'[{Style.BRIGHT}{Fore.RED}{self.current_mod.capitalize()}{Fore.RESET}{Style.RESET_ALL}] Doks {Style.BRIGHT}{Fore.RED}>>{Fore.RESET}{Style.RESET_ALL} ')
            

            if self.input.split(" ")[0] == "mod":
                if self.input.split(" ")[1].capitalize() in self.mod:
                    self.current_mod = self.input.split(" ")[1].strip(" ").capitalize()

            elif self.input.split(" ")[0] == "back":
                self.current_mod = self.mod[0]
                
            
            elif self.input.split(" ")[0] == "show":
                print("im in showw")
                if self.current_mod ==  self.mod[0]:
                    print(
                        '''
                        test
                        '''
                    )
                elif self.current_mod ==  self.mod[1]:
                    pass
                elif self.current_mod ==  self.mod[2]:
                    pass

            elif self.input.strip(" ") == "exit":
                print("\nGoodbye !")
                sleep(3)
                sys.exit()
