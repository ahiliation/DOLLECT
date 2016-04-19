# -*- coding: utf-8 -*-
import wget
import sys
import os

global stringa
global stringb
stringa = "(TRANS...> "
stringb = ".pdf"

off = list()
off.append('how-to-make-mistakes-in-python.pdf')
off.append('object-oriented-vs-functional-programming.pdf')
off.append('analyzing-visualizing-data-f-sharp.pdf')
off.append('java-the-legend.pdf')
off.append('why-rust.pdf')
off.append('introducing-java-8.pdf')
off.append('engineering-managers-guide-design-patterns.pdf')
off.append('azure-for-developers.pdf')
off.append('c++-today.pdf')
off.append('functional-programming-python.pdf')
off.append('python-in-education.pdf')
off.append('from-future-import-python.pdf')
off.append('software-architecture-patterns.pdf')
off.append('migrating-cloud-native-application-architectures.pdf')
off.append('getting-started-with-innersource.pdf')

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


def links():
    try:
        print "Links"
        print "http://learnyouahaskell.com/chapters"
        print "http://www.minimalprogramming.org/html/index.html"
        print "http://book.realworldhaskell.org/read/"
        print "http://dev.stephendiehl.com/fun/"
        print "http://c.codeindepth.com/"
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
        if i <= 16:
#           print stringa + stringh  + str(i) + stringb
            convertednext = decimal_roman(i)
            print stringa + " " +"LINUXVOICE" + " " + convertednext
            filename = wget.download(a+b)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"


def oreilly():
    stringi  = "https://www.oreilly.com/"
    stringj = "programming/free/files/"
    e = stringi + stringj
    for count in xrange(len(off)):
        f = off[count]
        print stringa + f 
        filename = wget.download(e+f)
        print ("\n Completed \n")

if len(sys.argv) > 1:
    if sys.argv[1] == "lv" and len(sys.argv) == 3:
        if int(sys.argv[2]) <= 9:
#            print "hello"
            i = int(sys.argv[2])
            lva()
            sys.exit(0)
        elif int(sys.argv[2]) <= 16:
            #debug
            i = int(sys.argv[2])
            lvb()
            sys.exit(0)
    elif sys.argv[1] == "oreilly":
        oreilly()
        
    elif sys.argv[1] == "tldp":
        tldp()
        
    elif sys.argv[1] == "floss":
        floss()

    elif sys.argv[1] == "links":
        links()
    
    else:
        print "\n LINUXVOICE COMPLETE \n"
        for i in xrange(16):
            if i == 0:
                continue
            if i <= 9:
                lva()
            else:
                lvb()
                                                            
