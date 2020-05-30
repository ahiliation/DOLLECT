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
no = 3

y = 3 


link = "https://dl.acm.org/toc/cacm/"+ str(year) +  "/" + str(vol) + "/" + str(no)
#print (link)
initial = requests.get(link, allow_redirects=True)
#print(initial)

open("index.html", 'wb').write(initial.content)
# print (index)
dpage = open("index.html" , "rt") 
contents = dpage.read()      # read the entire file into a string
dpage.close()   

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "lxml")



strfile = contents.find('doi')
#print (type(strfile))
#newstr = strfile[4:10]
#print (newstr)
#print  (strfile)
#print (type(contents))
#print (contents[412:418])
newstr = contents[466:485]
#print  (newstr)
newcontents = newstr[5:]
#print (newcontents)



#soup = BeautifulSoup(html, 'html.parser')
#documentname = soup.find_all('h5')
for x in [1,3]:
    documentname = soup.find_all('h5')
    print (documentname[x].a.contents[0])

print (type(documentname))
#print (documentname)


linknumber = 368718
newlink = "https://dl.acm.org/doi/pdf/" + newcontents + "." + str(linknumber)
#newlink = "https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.6.15.tar.xz"
r = requests.get(newlink, allow_redirects=True, stream=True)
print (dir(r.url.title))
print (r.url)
# print (type(r))
# Total size in bytes.                                                                                                 t
# total_size = int(r.headers.get('content-length', 0))
total_size = int(r.headers.get('content-length', 0))
#total_size = int(r.headers.get('content-length', 0))/(32*1024))
#total_size = 208896
print (total_size)
block_size = 1024 #1 Kibibyte                                                                                          
t=tqdm(total=total_size, unit='B', unit_scale=True)
with open(documentname[1].a.contents[0] + "." + "pdf", 'wb') as f:
    for data in r.iter_content(block_size):
       # sleep(0.1)
        t.update(len(data))
        f.write(data)
t.close()
if total_size != 0 and t.n != total_size:
    print("ERROR, something went wrong")
              
    #print (newlink)
#print ("hello")
#solfile = requests.get(newlink, allow_redirects=True)
#open(documentname[1].a.contents[0] + "." + "pdf", 'wb').write(solfile.content)

for i in [3]:
    linknumber = i + linknumber
    newlink = "https://dl.acm.org/doi/pdf/" + newcontents + "." + str(linknumber)
  #  print (newlink)
    solfile = requests.get(newlink, allow_redirects=True)
  #  print (type(solfile))
    open(documentname[3].a.contents[0] + "." + "pdf", 'wb').write(solfile.content)

