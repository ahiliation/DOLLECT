import wget
import sys
import urllib

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
                # ds = dollect string
                ds = "/manual/"
                if self.base == "http://www.gnu.org/software/trans-coord/manual/":
                    ds = "/"
                html = self.base + self.program + ds + self.program + ".html"
                info = self.base + self.program + ds + self.program + "-info.tar.gz"
                text = self.base + self.program + ds + self.program + ".txt"
                dvi  = self.base + self.program + ds + self.program + ".dvi.gz"
                pdf  = self.base + self.program + ds + self.program + ".pdf"
                texi = self.base + self.program + ds + self.program + ".texi.tar.gz"
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
          		            
			        
  

#data = GNUDollect("http://www.gnu.org/software/", "mdk")
#dict = GNUDollect("http://puszcza.gnu.org.ua/software/", "dico")

#data.Pownload()
#dict.Pownload()
#data.Pownload()

def connectivity():
        check = "https://www.google.co.in"
        print "Internet Connectivity.........",
        try:
            data = urllib.urlopen(check)
            print "Available"
        except:
            print "Failed\n"
            sys.exit(0)

def link(accept):
#    print type(accept)
    if  accept == "archiving" or accept == "audio" or accept == "database":
        basegnu = "http://www.gnu.org/software/"
        return basegnu
    elif accept == "dictionaries":
        basegnu = "http://puszcza.gnu.org.ua/software/"
        return basegnu
    elif accept == "doculation": 
        basegnu = "http://www.gnu.org/software/trans-coord/manual/"
        return basegnu
    elif accept == "education" :
        basegnu = "http://www.gnu.org/software/"
        return basegnu



def archiving(formataccept):
        print "[Cpio/Gzip/Paxutils/Sharutils/Tar/Xorriso]"
        selection = raw_input()
        program = selection.lower()
        archive = GNUDollect("http://www.gnu.org/software/", program)
	archive.Pownload()


def audio(formataccept):
#    print "hello"                                                                                                            
    audio = list()
    audio.append('Ccd2cue')
    audio.append('EMMS')
    audio.append('Gmediaserver')
    audio.append('GNUfm')
    audio.append('GNUmp3d')
    audio.append('GNUpod')
    audio.append('Radio')
    audio.append('GNUsound')
    audio.append('Guile-SDL')
    audio.append('Libcdio')
    audio.append('Libextractor')
    audio.append('Speex')
    audio.append('Xhippo')
    print "[Ccd2cue/EMMS/Gmediaserver/GNUfm/GNUmp3d/GNUpod/Radio/]"
    print "[GNUsound/Guile-SDL/Libcdio/Libextractor/Speex/Xhippo]"
    selection = raw_input()
    program = selection.lower()
    audio = GNUDollect("http://www.gnu.org/software/", program)
    audio.Pownload()

def database(): 
    database = list()
    database = ['Gdbm','Libdbh']
    print "[Gdbm/Libdbh]"
    selection = raw_input()
    if selection == "Libdbh":
        program = "Libdbh"
        leaf  = selection.lower()
    else:
        print "hello"
        program = selection.lower()
        leaf = selection.lower()
    database = GNUDollect("http://www.gnu.org/software/" , program)
    database.Pownload()


def dictionaries():
    dictionaries = list()
    dictionaries = ['Dico']
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Dico]"
    selection = raw_input()
    program = selection.lower()
    base = link("dictionaries")
    dictionaries = GNUDollect(base , program)
    dictionaries.Pownload()


def doculation():
#    print "hello" 
    doculation = list()
    doculation = ['WEB-TRANS','GNUN']
    print "[WEB-TRANS/GNUN]"
    selection = raw_input()
    program = selection.lower()
  #  print program
    base = link("doculation")
    doculation = GNUDollect(base , program)
    doculation.Pownload()


def editor():
#   print "hello" 
    editor = list()
    editor = ['Moe','nano']
    print "[Moe/nano]"
    selection = raw_input()
    if selection == "Moe":
        filename = wget.download("http://www.gnu.org/software/moe/manual/moe_manual.html")
        print "\n"
    elif selection == "nano":
        filename = wget.download("http://www.nano-editor.org/dist/v2.5/nano.html")
        print "\n"
    else:
        sys.exit(0)



if len(sys.argv) > 1:
    if sys.argv[1] == "lv" and len(sys.argv) == 3:
        if int(sys.argv[2]) <= 9:
#            print "hello"
            i = int(sys.argv[2])
            connectivity()
            lva()
            sys.exit(0)
        elif int(sys.argv[2]) <= 18:
            #debug
            i = int(sys.argv[2])
            connectivity()
            lvb()
            sys.exit(0)
    elif sys.argv[1] == "oreilly":
        connectivity()
        selection = raw_input('programming/data \n')
        oreilly(selection)
        
    elif sys.argv[1] == "tldp":
        connectivity()
        tldp()
        
    elif sys.argv[1] == "floss":
        connectivity()
        floss()

    elif sys.argv[1] == "links":
        connectivity()
        links()
        
    elif sys.argv[1] == "gcc":
        connectivity()
        gcc()

    elif sys.argv[1] == "gdb":
        connectivity()
        gdb()
        
    elif sys.argv[1] == "archiving":
#        print "hello"
        connectivity()
        archiving("NULL")

    elif sys.argv[1] == "audio":
        connectivity()
        audio("NULL")

    elif sys.argv[1] == "database":
        connectivity()
        database()

    elif sys.argv[1] == "dictionaries":
        connectivity()
        dictionaries()

    elif sys.argv[1] == "doculation":
        connectivity()
        doculation()

    elif sys.argv[1] == "editor":
        connectivity()
        editor()
        
    elif sys.argv[1] == "education":
        connectivity()
        education()
        
    elif sys.argv[1] == "email":
        connectivity()
        email()

    elif sys.argv[1] == "font":
        connectivity()
        font()

    elif sys.argv[1] == "organization":
        connectivity()
        organization()

    elif sys.argv[1] == "game":
        connectivity()
        game()

    elif sys.argv[1] == "graphics":
        connectivity()
        graphics()

    elif sys.argv[1] == "health":
        connectivity()
        health()

    elif sys.argv[1] == "alltext":
        connectivity()
        alltext()
        
    else:
        print "\n LINUXVOICE COMPLETE \n"
        for i in xrange(18):
            if i == 0:
                continue
            if i <= 9:
                connectivity()
                lva()
            else:
                connectivity()
                lvb()

