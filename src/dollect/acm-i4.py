import requests
import h11
#import re
import wget
import urllib
import sys
import os
from bs4 import BeautifulSoup 
import lxml
import time
from time import sleep
from tqdm import tqdm

year = 1958
vol  = 1
no = 4

y = 3


link = "https://dl.acm.org/toc/cacm/"+ str(year) +  "/" + str(vol) + "/" + str(no)
initial = requests.get(link, allow_redirects=True)

open("index.html", 'wb').write(initial.content)
dpage = open("index.html" , "rt") 
contents = dpage.read()      # read the entire file into a string
dpage.close()   

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "lxml")



strfile = contents.find('doi')
print  (strfile)
newstr = contents[471:485]
newcontents = newstr

for x in [1,3,5]:
    documentname = soup.find_all('h5')
    print (documentname[x].a.contents[0])

print (type(documentname))
#print (documentname)


linknumber = 368802
newlink = "https://dl.acm.org/doi/pdf/" + newcontents + "." + str(linknumber)
print (newlink)
solfile = requests.get(newlink, allow_redirects=True)
open(documentname[1].a.contents[0] + "." + "pdf", 'wb').write(solfile.content)

for i in [3,6]:
    linknumber = i + linknumber
    newlink = "https://dl.acm.org/doi/pdf/" + newcontents + "." + str(linknumber)
    solfile = requests.get(newlink, allow_redirects=True)
    open(documentname[y].a.contents[0] + "." + "pdf", 'wb').write(solfile.content)
    y = y + 2
