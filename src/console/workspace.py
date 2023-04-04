import readline
from colorama import Style

class Interact():
    #intitle:"index of /" intext:".env"

    def __init__(self) -> None:
        self.mod = ['Work', 'Search', 'Insert']
        self.in_mod = False
        self.current_mod = ''
        self.cmd_on_mod = []
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
        if self.in_mod :
            self.cmd_on_mod = list(self.cmd['mod '][self.current_mod+" "].keys()).pop("discrib")
            return
        
        self.cmd_on_mod = self.cmd.keys()

    def console(self):
    
        self.current_mod = self.mod[0]
        while True:
            self._tab_maker()
            readline.set_completer(self._tab)
            readline.parse_and_bind('tab: complete')
            commande = input(f'[{self.current_mod}] Doks >> ')
            # traitez la commande ici...

            if commande.split(" ")[0] == "mod":
                self.current_mod = commande.split(" ")[1]
                self.in_mod = True

