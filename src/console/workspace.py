import readline
from colorama import Style
from .tab import tabs_in_mod
import sys
from time import sleep


class Interact():
    #intitle:"index of /" intext:".env"

    def __init__(self) -> None:
        self.mod = ['Work', 'Search', 'Insert']
        self.current_mod = ''
        self.cmd_on_mod = []
        self.tab_in_mod = tabs_in_mod
        self.input = ""
        self.cmd = {
            'mod ':{
                'insert ':{
                    'use' : '',
                    'set' : '',
                    'show': '',
                    'discrib': ''
                },
                'search ' :{
                    'use' : '',
                    'set' : '',
                    'show': '',
                    'discrib': ''
                }
            },           
            'help ':{
                'discrib': ''
            },
            'exit ':{
                'discrib': ''
            },
            'show ':{
                'discrib': ''
            }
        }
        
    def _tab(self, text, state):
        options = self.cmd_on_mod
        matches = [option for option in options if option.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None
    
    def _tab_maker(self):
        if self.current_mod :
            self.cmd_on_mod = self.tab_in_mod[self.current_mod]
            return
        
        self.cmd_on_mod = self.cmd.keys()

    def console(self):
    
        self.current_mod = self.mod[0].strip(" ")
        while True:
            self._tab_maker()
            readline.set_completer(self._tab)
            readline.parse_and_bind('tab: complete')
            self.input = input(f'[{self.current_mod.capitalize()}] Doks >> ')
            # traitez la commande ici...

            if self.commande.split(" ")[0] == "mod":
                self.current_mod = self.commande.split(" ")[1]
                self.in_mod = True
            
            elif self.commande.split(" ")[0] == "show":

                if self.current_mod ==  "work":
                    pass
                elif self.current_mod ==  "search":
                    pass
                elif self.current_mod ==  "insert":
                    pass

            elif self.commande.strip(" ") == "exit":
                print("\nGoodbye !")
                sleep(3)
                sys.exit()
