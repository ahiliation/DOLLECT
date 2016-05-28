import wget
import sys

global ds
global base
base = "initial"
global program
program = "initial"

dictionaries = list()
ds = list()
database = list()
form = list()
dlink = list()

class GNUDollect():
    def __init__(self, base, program):
        self.base = base
        self.program = program
        form.append('html')
        form.append('info')
        form.append('ascii')
        form.append('dvi')
        form.append('pdf')
        form.append('texi')
        html = base + program + "/manual/" + program + ".html"
        info = base + program + "/manual/" + program + "-info.tar.gz"
        text = base + program + "/manual/" + program + ".txt"
        dvi  = base + program + "/manual/" + program + ".dvi.gz"
        pdf  = base + program + "/manual/" + program + ".pdf"
        texi = base + program + "/manual/" + program + ".texi.tar.gz"
        dlink.append(html)
        dlink.append(info)
        dlink.append(text)
        dlink.append(dvi)
        dlink.append(pdf)
        dlink.append(texi)
                        
   # def __init__(self, ds):
   #     self.ds = ds
   # global html

    def pownload():
        print "[html/info/ascii/dvi/pdf/texi/all]"
        selection = raw_input()
#        for name in xrange(6):
        if selection == "all":
            for name in xrange(6):
                filename = wget.download(dlink[name])
            print "\n"
         #   sys.exit(0)
        else:
            for name in xrange(6):
                if selection == form[name]:
                    try:
                        filename = wget.download(dlink[name])
                        print "\n"
                    except:
                        print "Unable to find URL \n"



dictionaries.append('Dico')
#print "[Dico]"
#selection = raw_input()
#selection = selection.lower()
dict = GNUDollect("http://puszcza.gnu.org.ua/software/", "dico")
#dict.pownload()		            
			        
  

database.append('Gdbm')
database.append('Libdbh')
data = GNUDollect("http://www.gnu.org/software/", "Gdbm")
data.pownload()
#print "hello"
#dict.pownload(dictionaries)

