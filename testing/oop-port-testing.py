import wget
import sys
import urllib
import os

form = list()
dlink = list()



class GNUDollect():
        def __init__(self, base, program):
                self.base = base
                self.program = program
                
        def Path(self):
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

        def PathA(self):
                global html
                global info
                global text
                global dvi
                global pdf
                global texi
                html = self.base + self.program + ".html"
                info = self.base + self.program + "-info.tar.gz"
                text = self.base + self.program + ".txt"
                dvi  = self.base + self.program + ".dvi.gz"
                pdf  = self.base + self.program + ".pdf"
                texi = self.base + self.program + ".texi.tar.gz"

        def PathB(self):
                global html
                global info
                global text
                global dvi
                global pdf
                global texi
                html = self.base + self.program + "/manual/" + "en/" + self.program + ".html"
                info = self.base + self.program + "/manual/" + "en/" + self.program + "-info.tar.gz"
                text = self.base + self.program + "/manual/" + "en/" + self.program + ".txt"
                dvi  = self.base + self.program + "/manual/" + "en/" + self.program + ".dvi.gz"
                pdf  = self.base + self.program + "/manual/" + "en/" + self.program + ".pdf"
                texi = self.base + self.program + "/manual/" + "en/" + self.program + ".texi.tar.gz"


        def PathC(self):
                global html
                global targz
                global htmlgz
                global ps
                global pdf
                global pdfgz
                
                html =    self.base + self.program + "/manual/" + "user_ref/" + selection + ".html"
                targz =   self.base + self.program + "/manual/" + "user_ref/" + selection + ".tar.gz"
                htmlgz =  self.base + self.program + "/manual/" + "user_ref/" + selection + ".html.gz"
                ps  =     self.base + self.program + "/manual/" + "user_ref/" + selection + ".ps.gz"
                pdf  =    self.base + self.program + "/manual/" + "user_ref/" + selection + ".pdf"
                pdfgz =   self.base + self.program + "/manual/" + "user_ref/" + selection + ".pdf.gz"
                
        def Pownload(selection):
                form = ['html','info','ascii','dvi','pdf','texi']
                dlink = [html, info, text, dvi, pdf, texi]
                if selection == "3DLDF":
                        dlink.append(html)
                        dlink.append(targz)
                        dlink.append(htmlgz)
                        dlink.append(ps)
                        dlink.append(pdf)
                        dlink.append(pdfgz)
                        
                print "[html/info/ascii/dvi/pdf/texi/all]"
                selection = raw_input()
                if selection == "all":
                        for name in xrange(6):
                                filename = wget.download(dlink[name])
                        print "\n"
                        sys.exit(0)
                else:
                        for name in xrange(6):
                                if selection == form[name]:
                                        filename = wget.download(dlink[name])
                                        print "\n"
                                        sys.exit(0)
          		            
			        
  

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
    elif accept == "education" or "Anubis" :
        basegnu = "http://www.gnu.org/software/"
        return basegnu


def official(accept):
    if accept == "Dr.Geo":
        typeof = "non-standard"
        return typeof
    elif accept == "MIX Development Kit":
        typeof = "standard"
        return typeof
    elif accept == "Fontopia":
        typeof = "standard"
        return typeof
    elif (accept == "Acm" or accept == "GNUchess" or accept == "GNUbg" or
          accept == "GNUbik" or accept == "LiquidWar6" or accept == "XBoard" or
          accept == "Plotutils" or accept == "Guile-Opengl"):
        typeof = "standard"
        return typeof



def archiving(formataccept):
        print "[Cpio/Gzip/Paxutils/Sharutils/Tar/Xorriso]"
        selection = raw_input()
        program = selection.lower()
        archive = GNUDollect("http://www.gnu.org/software/", program)
        archive.Path()
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
    audio.Path()
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
    database.Path()
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
    dictionaries.Path()
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
    doculation.Path()
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



def education():
#    print "hello" 
    education = list()
    education.append('Dr.Geo')
    education.append('Eprints')
    education.append('FisicaLab')
    education.append('GCompris')
    education.append('Gradebook')
    education.append('Glean')
    education.append('GNUschool')
    education.append('Gtypist')
    education.append('Ignuit')
    education.append('MDK')
    print "[Dr.Geo/Eprints/FisicaLab/Gcompris/Gradebook/Glean/GNUschool]"
    print "[Gtypist/Ignuit/MDK]"
    selection = raw_input()
    # type = official(selection)
    program = selection.lower()
    base = link("education")
    if selection == "Dr.Geo":
         print "No data available"
         sys.exit(0)
    elif selection == "Eprints":
        filename = wget.download("http://wiki.eprints.org/w/EPrints_Manual")
        print "\n"
        sys.exit(0)
    elif selection == "FisicaLab":
        filename = wget.download(base + program + "/manual/en/fisicalab/index.html")
        print "\n"
        sys.exit(0)
    elif selection == "Gcompris":
        filename = wget.download("http://gcompris.net/wiki/Manual")
        print "\n"
        sys.exit(0)
    elif selection == "Gradebook":
        filename = wget.download("http://www.gnu.org/software/ggradebook/")
        print "\n"
        sys.exit(0)
    elif selection == "Glean":
        filename = wget.download("http://glean.eu/dir/")
        print "\n"
        sys.exit(0)
    elif selection == "GNUschool":
        filename = wget.download(base + program + "/gnuschool.html")
        print "\n"
        sys.exit(0)
    elif selection == "Gtypist":
        filename = wget.download(base + program+ "/doc/")
        print "\n"
        sys.exit(0)
    elif selection == "Ignuit":
        filename = wget.download("http://homepages.ihug.co.nz/~trmusson/programs.html#ignuit")
        print "\n"
        sys.exit(0)
	
    education = GNUDollect(base , program)
    education.Path()
    education.Pownload()



def email():
#    print "hello" 
    email = list()
    email.append('Anubis')
    email.append('GNUbiff')
    email.append('Mailman')
    email.append('Mailutils')
    print "[Anubis/GNUbiff/Mailman/Mailutils]"
    selection = raw_input()
    program = selection.lower()
  #  print program
    base = link("Anubis")
    if selection == "GNUbiff":
        filename = wget.download("http://gnubiff.sourceforge.net/documentation.php")
        print "\n"
        sys.exit(0)
    elif selection == "Mailman":
        base = "http://www.gnu.org/software/"
        filename = wget.download(base + program + "/mailman-member.pdf")
        print "\n"
        sys.exit(0)
    elif selection == "Mailutils":
         base = "http://mailutils.org/manual/"
         email = GNUDollect(base , program)
         email.PathA()
         email.Pownload()
         
    email = GNUDollect(base , program)
    email.Pownload()



def font():
#    print "hello" 
    font = list()
    font.append('Fontopia')
    font.append('Fontutils')
    font.append('FreeFont')
    font.append('Intlfonts')
    font.append('Unifont')
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Fontopia/Fontutils/FreeFont/Intlfonts/Unifont]"
    selection = raw_input()
    program = selection.lower()
    type = official(selection)
    if selection == "Fontutils":
        filename = wget.download("http://www.delorie.com/gnu/docs/fontutils/fontu_toc.html")
        print "\n"
        sys.exit(0)
    elif selection == "FreeFont":
        base = "http://www.gnu.org/software/"
        filename = wget.download(base +  "/freefont/design-notes.html")
        print "\n"
        sys.exit(0)
    elif selection == "Intlfonts":
       filename = wget.download("http://directory.fsf.org/wiki/Intlfonts")
       print "\n"
       sys.exit(0)
    elif selection == "Unifont":
       filename = wget.download("http://unifoundry.com/unicode-tutorial.html")
       print "\n"
       sys.exit(0)
                       
    elif type == "standard" :
        base = "http://www.gnu.org/software/"
        font = GNUDollect(base , program)
        font.Path()
        font.Pownload()


def organization():
    print "[ GNU organization ]"
    try:
        filename = wget.download("http://www.gnu.org/prep")
      #  print "\n name of the downloaded document is", filename
        os.rename ('prep', 'prep.html') 
    except:
        print "hello"
  #  for method in dir(wget):
  #      if callable(getattr(wget, method)):
  #         print method
    print "\n"
    sys.exit(0)



def game():
#    print "hello" 
    game = list()
    game.append('Acm')
    game.append('BallandPaddle')
    game.append('GNUChess')
    game.append('Dominion')
    game.append('GNUbg')
    game.append('GNUbik')
    game.append('GNUgo')
    game.append('GNUjump')
    game.append('GNUkart')
    game.append('GNUrobots')
    game.append('GNUshogi')
    game.append('Leg')
    game.append('LiquidWar6')
    game.append('Motti')
    game.append('Rpge')
    game.append('Talkfilters')
    game.append('XBoard')
    print "[Acm/BallandPaddle/GNUChess/Dominion/GNUbg]"
    print "[GNUbik/GNUgo/GNUjump/GNUkart/GNUrobots/GNUshogi]"
    print "[Leg/LiquidWar6/Motti/Rpge/Talkfilters/XBoard]"
    selection = raw_input()
    program = selection.lower()
    type = official(selection)
    if type == "standard" :
        base = "http://www.gnu.org/software/"
        game = GNUDollect(base , program)
        game.Path()
        game.Pownload()
    elif selection == "GNUgo":
      #  print "hello"
        filename = wget.download("http://www.gnu.org/software/gnugo/gnugo_toc.html")
        print "\n"
        sys.exit(0)
    elif selection == "GNUrobots":
        filename = wget.download("http://www.gnu.org/software/gnurobots/readme.html")
        print "\n"
        sys.exit(0)
    elif selection == "Motti":
       filename = wget.download("http://www.gnu.org/software/motti/manual/")
       print "\n"
       sys.exit(0)
    elif selection == "Rpge":
       filename = wget.download("http://www.gnu.org/software/rpge/rpge.pdf")
       print "\n"
       sys.exit(0)
    elif selection == "Talkfilters":
       filename = wget.download("http://www.hyperrealm.com/talkfilters/talkfilters.pdf")
       print "\n"
       sys.exit(0)
    else:
        print "\n"
        sys.exit(0)


def graphics():
#    print "hello" 
    graphics = list()
    graphics.append('3DLDF')
    graphics.append('Dia')
    graphics.append('GIFT')
    graphics.append('GIMP')
    graphics.append('Gpaint')
    graphics.append('GSEgrafix')
    graphics.append('Guile-Opengl')
    graphics.append('MAVERIK')
    graphics.append('Panorama')
    graphics.append('Plotutils')
    graphics.append('XaoS')
    graphics.append('Libxmi')
    print "[3DLDF/Dia/GIFT/GIMP/Gpaint/GSEgrafix/Guile-Opengl]"
    print "[MAVERIK/Panorama/Plotutils/XaoS]"
    global selection
    selection = raw_input()
    program = selection.lower()
    type = official(selection)
    if type == "standard" :
        print "hello"
        base = "http://www.gnu.org/software/"
        graphics = GNUDollect(base, program)
        graphics.PathB()
        graphics.Pownload()

    elif selection == "3DLDF":
        base = "http://www.gnu.org/software/"
        graphics = GNUDollect(base, program)
        graphics.PathC()
        graphics.Pownload("3DLDF")
        
    elif selection == "Dia":
       # print "hello"
        filename = wget.download("http://dia-installer.de/doc/en/dia-manual.chm")
        print "\n"
        sys.exit(0)
    elif selection == "GIMP":
        filename = wget.download("http://www.gimp.org/man/gimp.html")
        print "\n"
        sys.exit(0)
    elif selection == "XaoS":
       filename = wget.download("http://xaos.sourceforge.net/doc-trunk/")
       print "\n"
       sys.exit(0)
    elif selection == "GSEgrafix":
       filename = wget.download("http://www.gnu.org/software/gsegrafix/")
       print "\n"
       sys.exit(0)
    elif selection == "MAVERIK":
       filename = wget.download("http://www.gnu.org/software/maverik/")
       print "\n"
       sys.exit(0)
    elif selection == "Libxmi":
       filename = wget.download("http://www.gnu.org/software/libxmi/")
       print "\n"
       sys.exit(0)
    else:
        print "\n"
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
