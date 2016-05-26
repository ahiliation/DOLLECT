# -*- coding: utf-8 -*-
import wget
import sys
import os
import urllib
from BeautifulSoup import *

global stringa
global stringb
global formataccept
formataccept = "initial"
global arca
arca = "initial"
global selection
selection = "initial"
global form
form = "initial"
global dlink
dlink = 0
global text
text = "initial"
stringa = "(TRANS...> "
stringb = ".pdf"


programming = list()
programming.append('how-to-make-mistakes-in-python.pdf')
programming.append('object-oriented-vs-functional-programming.pdf')
programming.append('analyzing-visualizing-data-f-sharp.pdf')
programming.append('java-the-legend.pdf')
programming.append('why-rust.pdf')
programming.append('introducing-java-8.pdf')
programming.append('engineering-managers-guide-design-patterns.pdf')
programming.append('azure-for-developers.pdf')
programming.append('c++-today.pdf')
programming.append('functional-programming-python.pdf')
programming.append('python-in-education.pdf')
programming.append('from-future-import-python.pdf')
programming.append('software-architecture-patterns.pdf')
programming.append('migrating-cloud-native-application-architectures.pdf')
programming.append('getting-started-with-innersource.pdf')

data = list()
data.append('evaluating-machine-learning-models.pdf')
data.append('going-pro-in-data-science.pdf')
data.append('ten-signs-of-data-science-maturity.pdf')
data.append('what-is-data-science.pdf')
data.append('data-driven.pdf')
data.append('what-is-database-design-anyway.pdf')


def decimal_roman(count):
    input = int(count)
#[debug]    print input
#[debug]    print type(input)
    roman = []
#    del roman[:]
    while input >= 1000:
        roman.append("M")
        input -= 1000
    while input >= 500:
        roman.append("D")
        input -= 500
    while input >= 100:
        roman.append("C")
        input -= 100
    while input >= 50:
        roman.append("L")
        input -= 50
    while input >= 10:
        roman.append("X")
        input -= 10
    while input >= 5:
        roman.append("V")
        input -= 5
    while input >= 1:
        roman.append("I")
        input -= 1
    back = ''.join(roman)
    return back

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



def alltext():
    archiving("alltext")
    audio("alltext")
    

def processing(receivetext):
    filename = wget.download(receivetext)
    
    
    
def archiving(formataccept):
#    print "hello" 
    arca = list()
    form = list()
    dlink = list()
    arca = ['Cpio','Gzip','Paxutils','Sharutils','Tar','Xorriso']
    form = ['html','info','ascii','dvi','pdf','texi']
    if formataccept == "alltext":
        for package in arca:
            selection = package
            program = selection.lower()
            type = official(selection)
            base = link("archiving")

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
            processing(text)
            print package
    else:
        print "[Cpio/Gzip/Paxutils/Sharutils/Tar/Xorriso]"
        selection = raw_input()
        program = selection.lower()
        type = official(selection)
        base = link("archiving")

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
        for name in xrange(len(arca)):
            if arca[name] == selection:
                print "[html/info/ascii/dvi/pdf/texi/all]"
                selection = raw_input()
                for name in xrange(6):
                    if selection == "all":
                        for name in xrange(6):
                            filename = wget.download(dlink[name])
                        print "\n"
                        sys.exit(0)
                    else:
                        if form[name] == selection:
                            try:
                                filename = wget.download(dlink[name])
                                print "\n"
                            except:
                                print "Unable to find URL \n"


                    
                    
                    
def audio(formataccept):
#    print "hello" 
    audio = list()
    form = list()
    dlink = list()
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
    form = ['html','info','ascii','dvi','pdf','texi']
    if formataccept == "alltext":
        for package in audio:
            selection = package
            program = selection.lower()
            type = official(selection)
            base = link("audio")
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
            processing(text)
    else:
        print "[Ccd2cue/EMMS/Gmediaserver/GNUfm/GNUmp3d/GNUpod/Radio/]"
        print "[GNUsound/Guile-SDL/Libcdio/Libextractor/Speex/Xhippo]"
        selection = raw_input()
        program = selection.lower()
        base = link("audio")
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
        for name in xrange(len(audio)):
            if audio[name] == selection:
#            print "hello"
                print "[html/info/ascii/dvi/pdf/texi/all]"
                selection = raw_input()
                for name in xrange(6):
                    if selection == "all":
                        for name in xrange(6):
                            filename = wget.download(dlink[name])
                        print "\n"
                        sys.exit(0)
                    else:
                        if form[name] == selection:
                            try:
                                filename = wget.download(dlink[name])
                                print "\n"
                            except:
                                print "Unable to find URL \n"



def database():
#    print "hello" 
    database = list()
    form = list()
    dlink = list()
    database = ['Gdbm','Libdbh']
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Gdbm/Libdbh]"
    selection = raw_input()
    if selection == "Libdbh":
        program = "Libdbh"
        leaf  = selection.lower()
    else:
        program = selection.lower()
        leaf = selection.lower()
    base = link("database")
    html = base + leaf + "/manual/" + program + ".html"
    info = base + leaf + "/manual/" + program + "-info.tar.gz"
    text = base + leaf + "/manual/" + program + ".txt"
    dvi  = base + leaf + "/manual/" + program + ".dvi.gz"
    pdf  = base + leaf + "/manual/" + program + ".pdf"
    texi = base + leaf + "/manual/" + program + ".texi.tar.gz"
    dlink.append(html)
    dlink.append(info)
    dlink.append(text)
    dlink.append(dvi)
    dlink.append(pdf)
    dlink.append(texi)
    for name in xrange(len(database)):
        if database[name] == selection:
#            print "hello"
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"


def dictionaries():
#    print "hello" 
    dictionaries = list()
    form = list()
    dlink = list()
    dictionaries = ['Dico']
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Dico]"
    selection = raw_input()
    program = selection.lower()
    base = link("dictionaries")
    html = base + program + "/manual/" + program + ".html"
    info = base + program + "/manual/" + program + "-info.tar.gz"
    text = base + program + "/manual/" + program + ".txt"
    dvi  = base + program + "/manual/" + program + ".dvi.gz"
    pdf  = base + program + "/manual/" + program + ".pdf"
    texi = base + program + "/manual/" + program + ".texi.tar.gz"
#    print html
    dlink.append(html)
    dlink.append(info)
    dlink.append(text)
    dlink.append(dvi)
    dlink.append(pdf)
    dlink.append(texi)
    for name in xrange(len(dictionaries)):
 #       print dictionaries[name]
        if dictionaries[name] == selection:
#            print "hello"
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"

def doculation():
#    print "hello" 
    doculation = list()
    form = list()
    dlink = list()
    doculation = ['WEB-TRANS','GNUN']
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[WEB-TRANS/GNUN]"
    selection = raw_input()
    program = selection.lower()
  #  print program
    base = link("doculation")
    html = base + program + "/" + program + ".html"
    info = base + program + "/" + program + "-info.tar.gz"
    text = base + program + "/" + program + ".txt"
    dvi  = base + program + "/" + program + ".dvi.gz"
    pdf  = base + program + "/" + program + ".pdf"
    texi = base + program + "/" + program + ".texi.tar.gz"
    dlink.append(html)
    dlink.append(info)
    dlink.append(text)
    dlink.append(dvi)
    dlink.append(pdf)
    dlink.append(texi)
#    print "hello"
    for name in xrange(len(doculation)):
 #       print doculation[name]
        if doculation[name] == selection:
#            print "hello"
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"


def editor():
#   print "hello" 
    editor = list()
    form = list()
    dlink = list()
    editor = ['Moe','nano']
   # form = ['html','info','ascii','dvi','pdf','texi']
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
    form = list()
    dlink = list()
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
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Dr.Geo/Eprints/FisicaLab/Gcompris/Gradebook/Glean/GNUschool]"
    print "[Gtypist/Ignuit/MDK]"
    selection = raw_input()
    # type = official(selection)
    program = selection.lower()
    base = link("education")
    html = base + program + "/manual/" + program + ".html"
    info = base + program + "/manual/" + program + "-info.tar.gz"
    text = base + program + "/manual/" + program + ".txt"
    dvi  = base + program + "/manual/" + program + ".dvi.gz"
    pdf  = base + program + "/manual/" + program + ".pdf"
    texi = base + program + "/manual/" + program + ".texi.tar.gz"
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
        
    dlink.append(html)
    dlink.append(info)
    dlink.append(text)
    dlink.append(dvi)
    dlink.append(pdf)
    dlink.append(texi)
    
    # loop for selecting  package
    for name in xrange(len(education)):
        if education[name] == selection:
#            print "hello"
            # loop for selecting package format
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    print selection
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"



def email():
#    print "hello" 
    email = list()
    form = list()
    dlink = list()
    email.append('Anubis')
    email.append('GNUbiff')
    email.append('Mailman')
    email.append('Mailutils')
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Anubis/GNUbiff/Mailman/Mailutils]"
    selection = raw_input()
    program = selection.lower()
  #  print program
   # base = link("email")
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
         html = base + program + ".html"
         info = base + program + "-info.tar.gz"
         text = base + program + ".txt"
         dvi  = base + program + ".dvi.gz"
         pdf  = base + program + ".pdf"
         texi = base + program + ".texi.tar.gz"

    elif selection == "Anubis":
        base = "http://www.gnu.org/software/"
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
    
#    print "hello"
    for name in xrange(len(email)):
 #       print email[name]
        if email[name] == selection:
#            print "hello"
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"


def font():
#    print "hello" 
    font = list()
    form = list()
    dlink = list()
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
    
#    print "hello"
    for name in xrange(len(font)):
 #       print font[name]
        if font[name] == selection:
#            print "hello"
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"


def organization():
    print "[ GNU organization]"
    try:
        filename = wget.download("http://www.gnu.org/prep")
        print "name of the downloaded document is", filename
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
    form = list()
    dlink = list()
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
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Acm/BallandPaddle/GNUChess/Dominion/GNUbg]"
    print "[GNUbik/GNUgo/GNUjump/GNUkart/GNUrobots/GNUshogi]"
    print "[Leg/LiquidWar6/Motti/Rpge/Talkfilters/XBoard]"
    selection = raw_input()
    program = selection.lower()
    type = official(selection)
    if type == "standard" :
        base = "http://www.gnu.org/software/"
        html = base + program + "/manual/" + program + ".html"
        info = base + program + "/manual/" + program + "-info.tar.gz"
        text = base + program + "/manual/" + program + ".txt"
        dvi  = base + program + "/manual/" + program + ".dvi.gz"
        pdf  = base + program + "/manual/" + program + ".pdf"
        texi = base + program + "/manual/" + program + ".texi.tar.gz"
        
    elif selection == "GNUgo":
        print "hello"
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
                       
    
        
    dlink.append(html)
    dlink.append(info)
    dlink.append(text)
    dlink.append(dvi)
    dlink.append(pdf)
    dlink.append(texi)
    
#    print "hello"
    for name in xrange(len(game)):
 #       print game[name]
        if game[name] == selection:
#            print "hello"
            print "[html/info/ascii/dvi/pdf/texi/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"


def graphics():
#    print "hello" 
    graphics = list()
    form = list()
    dlink = list()
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
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[3DLDF/Dia/GIFT/GIMP/Gpaint/GSEgrafix/Guile-Opengl]"
    print "[MAVERIK/Panorama/Plotutils/XaoS]"
    selection = raw_input()
    program = selection.lower()
    type = official(selection)
    if type == "standard" :
        print "hello"
        base = "http://www.gnu.org/software/"
        html = base + program + "/manual/" + "en/" + program + ".html"
        info = base + program + "/manual/" + "en/" + program + "-info.tar.gz"
        text = base + program + "/manual/" + "en/" + program + ".txt"
        dvi  = base + program + "/manual/" + "en/" + program + ".dvi.gz"
        pdf  = base + program + "/manual/" + "en/" + program + ".pdf"
        texi = base + program + "/manual/" + "en/" + program + ".texi.tar.gz"

    elif selection == "3DLDF":
        base = "http://www.gnu.org/software/"
        html =    base + program + "/manual/" + "user_ref/" + selection + ".html"
        targz =   base + program + "/manual/" + "user_ref/" + selection + ".tar.gz"
        htmlgz =  base + program + "/manual/" + "user_ref/" + selection + ".html.gz"
        ps  =     base + program + "/manual/" + "user_ref/" + selection + ".ps.gz"
        pdf  =    base + program + "/manual/" + "user_ref/" + selection + ".pdf"
        pdfgz =   base + program + "/manual/" + "user_ref/" + selection + ".pdf.gz"
        
        
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
    elif selection == "MAVERIK":
       filename = wget.download("http://www.gnu.org/software/maverik/")
       print "\n"
       sys.exit(0)
    else:
        print "\n"
        sys.exit(0)
                       
    if selection == "3DLDF":
        dlink.append(html)
        dlink.append(targz)
        dlink.append(htmlgz)
        dlink.append(ps)
        dlink.append(pdf)
        dlink.append(pdfgz)
    elif type == "standard":
        dlink.append(html)
        dlink.append(info)
        dlink.append(text)
        dlink.append(dvi)
        dlink.append(pdf)
        dlink.append(texi)
        
#    print "hello"
    for name in xrange(len(graphics)):
        if graphics[name] == selection:
#            print "hello"
            if type == "standard":
                print "[html/info/ascii/dvi/pdf/texi/all]"
            elif selection == "3DLDF":
                print "[html/targz/htmlgz/ps/pdf/pdfgz/all]"
            selection = raw_input()
            for name in xrange(6):
                if selection == "all":
                    for name in xrange(6):
                        filename = wget.download(dlink[name])
                    print "\n"
                    sys.exit(0)
                else:
                    if form[name] == selection:
                        try:
                            filename = wget.download(dlink[name])
                            print "\n"
                        except:
                            print "Unable to find URL \n"
    
def health():
#    print "hello" 
    health = list()
    health.append('GNUmed')
    health.append('GNUtrition')
    health.append('GNUhealth')
   # form = ['html','info','ascii','dvi','pdf','texi']
    print "[GNUmed/GNUtrition/GNUhealth]"
    selection = raw_input()
    if selection == "GNUmed":
        filename = wget.download("http://www.gnumed.de/promotion/GNUmed-introduction_v4.pdf")
        print "\n"
        sys.exit(0)
    elif selection == "GNUtrition":
        filename = wget.download("http://www.gnu.org/software/gnutrition/manual/index.html")
        print "\n"
        sys.exit(0)
    elif selection == "GNUhealth":
       filename = wget.download("https://en.wikibooks.org/wiki/GNU_Health")
       print "\n"
       sys.exit(0)
    else:
        print "\n"
        sys.exit(0)
                       



    
def gdb():
    try:
        gdb = dict()
        pre1 = "http://sourceware.org/gdb/current/onlinedocs/"
        pre2 = "https://sourceware.org/gdb/talks/esc-west-1999/"
        gdb[1] = pre1 + "gdb.pdf.gz"
        gdb[2] = pre2 + "paper.pdf"
        gdb[3] = pre2 + "slides.pdf"
        print stringa
        print "GDB Documentation"
        print "GDB User Manual"
        filename = wget.download(gdb[1])
        print "\nThe Heisenberg Debugging Technology"
        print "Slides/Paper/Enter(for both)"
        decision = raw_input()
        if decision == "Paper":
            filename = wget.download(gdb[2])
        elif decision == "Slides":
            filename = wget.download(gdb[3])
        else:
            for key in range(2,4):
#                print key
                filename = wget.download(gdb[key])
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ? \n"


def gcc():
    try:
        print stringa
        print "GCC Documentation"
        print "GCC Manual"
        pre = "https://gcc.gnu.org/onlinedocs/"
        filename = wget.download(pre + "gcc.pdf")
        print "\nGNU Fortran Manual"
        filename = wget.download(pre + "gfortran.pdf")
        print "\nGCJ Manual"
        filename = wget.download(pre + "gcj.pdf")
        print "\nCPP Manual"
        filename = wget.download(pre + "cpp.pdf")
        print "\nCompleted\n"
    except:
        print "\n Did something else happen ? \n"
        
def links():
    try:
        print "Links"
        print "http://learnyouahaskell.com/chapters"
        print "http://www.minimalprogramming.org/html/index.html"
        print "http://book.realworldhaskell.org/read/"
        print "http://dev.stephendiehl.com/fun/"
        print "http://c.codeindepth.com/"
        print "https://gcc.gnu.org/faq.html"
        print "http://www.gnu.org/software/emacs/manual/html_node/emacs/index.html"
        print "http://www.gnu.org/software/emacs/manual/html_node/eintr/index.html"
        print "http://www.gnu.org/software/emacs/manual/html_node/elisp/index.html"
        print "\nLink Opener/Tester"
        link = raw_input()
        html = urllib.urlopen(link)
       # print page.read()
        soup = BeautifulSoup(html)
        tags = soup('body')
        print tags
     #   print dir(body.text)
      #  content = body.text()
     #   print type(content)
     #   print content
     #   for line in fhand:
      #      print line.rstrip()
    except:
        print "\n Did something else happen ? \n"
    

def tldp():
    try:
        print stringa
        print "GNU/Linux HOWTOs"
        filename = wget.download("http://tldp.org/Linux-HOWTO-pdf.tar.gz")
        print "\nCompleted\n"
    except:
        print "\n Did something else happen ? \n"


def floss():
    try:
        print stringa
        print "FLOSS manuals"
        filename = wget.download("https://en.flossmanuals.net/_booki/command-line/command-line.pdf") 
        print "\nCompleted\n"
        
    except:
        print "\n Did something else happen ? \n"


def lva():
    stringc = "http://www.linuxvoice.com/issues/00"
    stringd = "/Linux-Voice-Issue-00"
    stringg = "Linux-Voice-Issue-00"
    c = stringc  + str(i)  + stringd 
    d =  str(i) + stringb
    try:
        if i >= 1:
#           print stringa  + stringg + str(i) + stringb
            converted = decimal_roman(i)
            print stringa + " " +"LINUXVOICE" + " " + converted 
            filename = wget.download(c+d)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"
    
def lvb():
    stringe = "/Linux-Voice-Issue-0"
    stringf = "http://www.linuxvoice.com/issues/0"
    stringh = "Linux-Voice-Issue-0"
    a = stringf + str(i)  + stringe 
    b = str(i) + stringb
    try:
        if i <= 18:
#           print stringa + stringh  + str(i) + stringb
            convertednext = decimal_roman(i)
            print stringa + " " +"LINUXVOICE" + " " + convertednext
            filename = wget.download(a+b)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"


def oreilly(accept):
    stringi = "https://www.oreilly.com/"
    if accept == "programming":
        stringj = "programming/free/files/"
        e = stringi + stringj
        print stringa,
        for count in xrange(len(programming)):
            f = programming[count]
            print f + "\n"
            filename = wget.download(e+f)
            print "\n"
        print ("\n Completed \n")
        sys.exit(0)
    elif accept == "data":
        stringk = "data/free/files/"
        datac = stringi + stringk
        print stringa
        for count in xrange(len(data)):
            dataf = data[count]
            print dataf
            filename = wget.download(datac + dataf)
            print "\n"
        print ("\n Completed \n")
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
