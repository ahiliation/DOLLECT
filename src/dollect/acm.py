import requests
import h11
#import re
import wget
import urllib3
import sys
import os


year = 1958
vol  = 1
no = 1

link = "https://dl.acm.org/toc/cacm/"+ str(year) +  "/" + str(vol) + "/" + str(no)
print (link)
initial = requests.get(link, allow_redirects=True)
#print(initial)
open('hello.txt', 'wb').write(initial.content)

dpage = open("hello.txt" , "rt") 
contents = dpage.read()      # read the entire file into a string
dpage.close()   
strfile = contents.find('doi')
print (type(strfile))
#newstr = strfile[4:10]
#print (newstr)
#print (strfile)
#print (type(contents))
print (contents[343:362])
newstr = contents[343:362]
newcontents = newstr[5:]
print (newcontents)
newlink = "https://dl.acm.org/doi/pdf/" + newcontents + "." + "368689"
print (newlink)
solfile = requests.get(newlink, allow_redirects=True)
open('hello', 'wb').write(solfile.content)
