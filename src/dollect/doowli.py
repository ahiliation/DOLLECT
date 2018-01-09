import wget
import requests
import urllib2

# february 2003

string1 = "https://archive.org/download/"
string2 = "Linux-Journal-"

global year 
year = 1993
global month
month = 2
global urlb
filetype = ".pdf"

# url = "https://archive.org/download/Linux-Journal-2013-02/Linux-Journal-2013-02.pdf"


def download_file(url):
    global urlb
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

def lj():
    global year
    global month
    global mag
    global urlb
    for countyear in xrange(24):
        year = year + 1
        print "year is ", year
        if  year == 1994:
            for countfirst in xrange(10):
                month = month + 1
                print "month is", month 
                if month > 9:
                    urla = string1 + string2 + str(year) + "-" + str(month) + "/"                     
                    urlb = string2 + str(year) + "-" + str(month)
                else:
                    urla = string1 + string2 + str(year) + "-" + "0" + str(month) + "/"
                    urlb =  string2 + str(year) + "-" + "0" + str(month)
                filetype = ".pdf"
                url = urla + urlb + filetype 
                decision = file_exists(url)
                if decision == True:
                    download_file(url)
                else:
	            continue
        else:
            month = 0
            for countmonth in xrange(12):
                month = month + 1
                print "month is ", month 
                if month > 9:
                    urla = string1 + string2 + str(year) + "-" + str(month) + "/"                     
                    urlb = string2 + str(year) + "-" + str(month)
                else:
                    urla = string1 + string2 + str(year) + "-" + "0" + str(month) + "/"
                    urlb =  string2 + str(year) + "-" + "0" + str(month)
                filetype = ".pdf"
                url = urla + urlb + filetype 
                decision = file_exists(url)
                if decision == True:
                    download_file(url)
                else:
	            continue
                
lj()
                      
        
	




