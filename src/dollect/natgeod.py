import wget
import requests
import urllib2

# september 22 1888

string1 = "https://archive.org/download/"
string2 = "05"

global year 
year = 1965
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

def file_exists(url):
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False





# download_file(url)
def natgeo1966():
    global year
    global month
    global mag
    global urlb
    year = year + 1
      #  print "year is ", year
    if  year == 1966:
        for countfirst in xrange(12):
            month = month + 1
           #     print "month is", month 
            if month > 9:
                urla = string1 + str(year) + "05/" + str(year)+ "-" + str(month)                     
                   # urlb = string2 + str(year) + "-" + str(month)
            else:
                urla = string1 + str(year) + "05/" + str(year)+ "-" + "0" + str(month)
                  #  urlb =  string2 + str(year) + "-" + "0" + str(month)
            filetype = ".pdf"
            url = urla + filetype 
            decision = file_exists(url)
            if decision == True:
                download_file(url)
            else:
	        continue
     
                
natgeo1966()
                      
        
	




