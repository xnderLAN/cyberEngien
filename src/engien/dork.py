from googlesearch import search
from colorama import Style, Fore, init
class Dork:
    def __init__(self, dork, result=10, dtype=None, target=None) -> None:
        self.dork = dork
        self.type = dtype
        self.target = target
        self.result = result
        self.urls = []
        #self.console_running = f'{Style.BRIGHT}{Fore.BLUE}[-]{Fore.RESET}{Style.RESET_ALL}]'
        self.console_ok  = f'{Style.BRIGHT}{Fore.GREEN}[+]{Fore.RESET}{Style.RESET_ALL}'
        #self.console_error = f'{Style.BRIGHT}{Fore.RED}[!]{Fore.RESET}{Style.RESET_ALL}]'

                
    def google(self):
        #query = 'intitle:"index of /" intext:".env"'
        init()

        for j in search(self.dork, tld="co.in", num=10, stop=self.result, pause=2):
            self.urls.append(j)
            print(self.console_ok + f" {j}")
        
        return self.urls