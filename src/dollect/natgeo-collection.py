#Copyright 2018  Jeffrin Jose T

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import wget
import requests
import urllib2

# september 22 1888

string1 = "https://archive.org/download/"
global year
global month
month = 0
global urlb
filetype = ".PDF"

# url = "https://archive.org/download/196605/1966-01.PDF"


def download_file(url):
    global urlb
    global month
    global year
    print "\n"
    print " National Geographic --- Year :", year , "Month:", month
    filename = wget.download(url) 

 #This function is related to https://gist.github.com/dehowell/884204 	
def file_avail(url):
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False


def natgc(pyear):
    global month
    global year
    year = pyear
    for countfirst in xrange(12):
        month = month + 1
           #     print "month is", month
        if year == 1966:
            number = "05"
        elif year == 1957:
            number = "03" 
        elif year == 1955:
            number = "NationalGeographic1955"
        if month > 9:
	    urla = string1 + str(year) + number + "/" + str(year)+ "-" + str(month) 	
            if year == 1955:
                urla = string1 + number + "/" + str(year)+ "-" + str(month)                             
        else:
            urla = string1 + str(year) + number + "/" + str(year)+ "-" + "0" + str(month) 
            if year == 1955: 
                urla = string1 + number + "/" + str(year)+ "-" + "0" +str(month)
        filetype = ".PDF"
        url = urla + filetype 
        decision = file_avail(url)
        if decision == True:
            download_file(url)
        else:
	    continue

     
                
#natgc(1966)
#natgc(1957)
#natgc(1955)                      
        
	




