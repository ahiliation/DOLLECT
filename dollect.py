import wget
import sys


global string1
global string2
string1 = "Retrieving...  "
string2 = ".pdf"

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
    string3 = "http://www.linuxvoice.com/issues/00"
    string4 = "/Linux-Voice-Issue-00"
    string7 = "Linux-Voice-Issue-00"
    c = string3  + str(i)  + string4 
    d =  str(i) + string2
    try:
        if i >= 1:
            print string1 + string7 + str(i) + string2
            filename = wget.download(c+d)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"
    
def lvb():
    string5 = "/Linux-Voice-Issue-0"
    string6 = "http://www.linuxvoice.com/issues/0"
    string8 = "Linux-Voice-Issue-0"
    a = string6 + str(i)  + string5 
    b = str(i) + string2
    try:
        if i <= 12:
            print string1 + string8  + str(i) + string2
            filename = wget.download(a+b)
            print "\nCompleted\n"
    except:
        print "\n Did something else happen ?  \n"


def oreilly():
    string9  = "https://www.oreilly.com/"
    string10 = "programming/free/files/"
    e = string9 + string10
    for count in xrange(len(off)):
        f = off[count]
        print string1 + f 
        filename = wget.download(e+f)
        print ("\n Completed \n")

if len(sys.argv) > 1:
    if sys.argv[1] == "lv" and len(sys.argv) == 3:
        if int(sys.argv[2]) <= 9:
            print "hello"
            i = int(sys.argv[2])
            lva()
            sys.exit(0)
        elif int(sys.argv[2]) <= 12:
            #debug
            i = int(sys.argv[2])
            lvb()
            sys.exit(0)
    elif sys.argv[1] == "oreilly":
        oreilly()
    else:
        print "\n All LinuxVoice Download \n"
        for i in xrange(12):
            if i == 0:
                continue
            if i <= 9:
                lva()
            else:
                lvb()
                                                            
