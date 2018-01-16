import urllib
import json
import sys

url = "http://archive.org/metadata/NationalGeographic1955"
input = urllib.urlopen(url).read()

info = json.loads(input)

print "\nTesting JSON related\n"

print type(info)

print info['files'][0]['name']
 
