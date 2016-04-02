import wget
import sys


global stringa
global stringb
stringa = "[transferring...]  "
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

def lva():
    stringc = "http://www.linuxvoice.com/issues/00"
    stringd = "/Linux-Voice-Issue-00"
    string7 = "Linux-Voice-Issue-00"
    c = stringc  + str(i)  + stringd 
    d =  str(i) + stringb
    try:
        if i >= 1:
            print stringa + string7 + str(i) + stringb
            filename = wget.download(c+d)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"
    
def lvb():
    string5 = "/Linux-Voice-Issue-0"
    string6 = "http://www.linuxvoice.com/issues/0"
    string8 = "Linux-Voice-Issue-0"
    a = string6 + str(i)  + string5 
    b = str(i) + stringb
    try:
        if i <= 16:
            print stringa + string8  + str(i) + stringb
            filename = wget.download(a+b)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"


def oreilly():
    string9  = "https://www.oreilly.com/"
    stringa0 = "programming/free/files/"
    e = string9 + stringa0
    for count in xrange(len(off)):
        f = off[count]
        print stringa + f 
        filename = wget.download(e+f)
        print ("\n Completed \n")

if len(sys.argv) > 1:
    if sys.argv[1] == "lv" and len(sys.argv) == 3:
        if int(sys.argv[2]) <= 9:
            print "hello"
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
    else:
        print "\n All LinuxVoice Download \n"
        for i in xrange(16):
            if i == 0:
                continue
            if i <= 9:
                lva()
            else:
                lvb()
                                                            
