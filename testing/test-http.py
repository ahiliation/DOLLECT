# import urllib2
# response = urllib2.urlopen('https://archive.org/download/Linux-For-You-Issue-78/Linux-For-You-78-2009-07.pdf')
# lfy.pdf = response.read()

from tqdm import tqdm
import requests
import os
#from progress.bar import Bar


file_url = "https://archive.org/download/Linux-For-You-Issue-78/Linux-\
For-You-78-2009-07.pdf"
 
r = requests.get(file_url, stream = True)
 
with open("lfy.pdf","wb") as pdf:
#    print (type(pdf))
#    bar = Bar('Processing', max=20) 
#    for i in range(20):   	
#   for i in Bar('Processing').iter(it):
#        for chunk in r.iter_content(chunk_size=1024):
        # writing one chunk at a time to pdf file
#            if chunk:
#                pdf.write(chunk)
#                bar.next()
#    bar.finish()
    total_size = int(r.headers['Content-Length'])
    for data in tqdm(r.iter_content(1024), total=total_size, unit='B', unit_scale=True):
	pdf.write(data)   

