from webcrawl.bugsmusic import BugsCrawler
from webcrawl.assembly import AssemblyCrawler

class Controller:
    def __init__:
        pass

    def exec(self, flag, url):
        if flag == 'a':
            a = AssemblyCrawler(url)
            a.scrap()
        elif flag == 'b':
            b = BugsCrawler(url)
            b.scrap()