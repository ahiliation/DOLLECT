import requests
import re

dpage = open("3.html", "rt") 
contents = dpage.read()      # read the entire file into a string
dpage.close()   
strfile = contents.find('doi')
#print (strfile)
#print (type(contents))
print (contents[491:511])

#url = 'https://dl.acm.org/doi/pdf/10.1145/3396208'
#myfile = requests.get(url, allow_redirects=True)
#open('hello.pdf', 'wb').write(myfile.content)
