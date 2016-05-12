# -*- coding: utf-8 -*-
import wget
import sys
import os
import urllib
from BeautifulSoup import *

global stringa
global stringb
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
    elif accept == "education":
        basegnu = "http://www.gnu.org/software/"
        return basegnu

def official(accept):
    if accept == "Dr.Geo":
        typeof = "non-standard"
        return typeof
    elif accept == "MIX Development Kit":
        typeof = "standard"
        return typeof
    
    

        
    
def archiving():
#    print "hello" 
    arca = list()
    form = list()
    dlink = list()
    arca = ['Cpio','Gzip','Paxutils','Sharutils','Tar','Xorriso']
    form = ['html','info','ascii','dvi','pdf','texi']
    print "[Cpio/Gzip/Paxutils/Sharutils/Tar/Xorriso]"
    selection = raw_input()
    program = selection.lower()
    base = link("archiving")
 #   print base
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



                    
                    
                    
def audio():
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
        if i <= 17:
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
        elif int(sys.argv[2]) <= 17:
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
        archiving()

    elif sys.argv[1] == "audio":
        connectivity()
        audio()

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
        
    else:
        print "\n LINUXVOICE COMPLETE \n"
        for i in xrange(17):
            if i == 0:
                continue
            if i <= 9:
                connectivity()
                lva()
            else:
                connectivity()
                lvb()
