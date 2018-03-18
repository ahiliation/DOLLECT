import urllib
import json
import sys
import wget

# url = "http://archive.org/metadata/NationalGeographic1955"

#x = -1

name = raw_input("item name? ")


#print "\nTesting JSON related\n"

#print type(info)

#print info['files'][0]['name']

urld = "http://archive.org/metadata/" + name

input = urllib.urlopen(urld).read()

info = json.loads(input)

# print type(info)
for key, value in info.iteritems():
   # x = x + 1
   # print key
   # print "\n"
   # print "hello"
   # if len(key) > 1:
    option = "all"
    if key == "files":
        for x in range(len(info[key])):
            if option == "all":
                url = "http://archive.org/download/" + name + "/" + info[key][x]['name']
                filename = wget.download(url)
            # print x  
            elif  info[key][x]['format'] == "Text PDF":
                url = "http://archive.org/download/" + name + "/" + info[key][x]['name']
                filename = wget.download(url)
