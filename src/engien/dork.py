from googlesearch import search

class Dork:
    def __init__(self, dork, result=10, dtype=None, target=None) -> None:
        self.dork = dork
        self.type = dtype
        self.target = target
        self.result = result
        self.urls = []
                
    def google(self):
        #query = 'intitle:"index of /" intext:".env"'
        
        for j in search(self.dork, tld="co.in", num=10, stop=self.result, pause=2):
            self.urls.append(j)
        
        return self.urls