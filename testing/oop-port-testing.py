import wget
import sys

form = list()
dlink = list()

class GNUDollect():
        def __init__(self, base, program):
                self.base = base
                self.program = program

        def Pownload(self):
                global html
                global info
                global text
                global dvi
                global pdf
                global texi
                html = self.base + self.program + "/manual/" + self.program + ".html"
                info = self.base + self.program + "/manual/" + self.program + "-info.tar.gz"
                text = self.base + self.program + "/manual/" + self.program + ".txt"
                dvi  = self.base + self.program + "/manual/" + self.program + ".dvi.gz"
                pdf  = self.base + self.program + "/manual/" + self.program + ".pdf"
                texi = self.base + self.program + "/manual/" + self.program + ".texi.tar.gz"
                form = ['html','info','ascii','dvi','pdf','texi']
                dlink = [html, info, text, dvi, pdf, texi]
                print "[html/info/ascii/dvi/pdf/texi/all]"
                selection = raw_input()
                if selection == "all":
                        for name in xrange(6):
                                filename = wget.download(dlink[name])
                        print "\n"
                       # sys.exit(0)
                else:
                        print "helloo"
                        for name in xrange(6):
                                if selection == form[name]:
                                        print dlink[name]
                                        filename = wget.download(dlink[name])
                                        print "\n"
          		            
			        
  

data = GNUDollect("http://www.gnu.org/software/", "mdk")
dict = GNUDollect("http://puszcza.gnu.org.ua/software/", "dico")

data.Pownload()
dict.Pownload()
data.Pownload()
