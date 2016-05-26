import wget

class Dollect:
    global html
    html = "http://www.gnu.org/philosophy/philosophy.html"
    def download(self):
        filename = wget.download(html)

dobject = Dollect()
dobject.download()
