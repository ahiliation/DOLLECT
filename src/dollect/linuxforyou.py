import progressbar
import requests
import urllib2

# february 2003

string1 = "https://archive.org/download/"
string2 = "Linux-For-You-Issue-"
string3 = "Linux-For-You"
string4 = "-"
global year 
year = 2002
global month
month = 1
global mag
mag = 0
global urlb
filetype = ".pdf"

# url = "https://archive.org/download/Linux-For-You-Issue-78/Linux-For-You-78-2009-07.pdf"


def download_file(url):
    global urlb
    local_filename = urlb + filetype
    r = requests.get(url, stream=True)
    f = open(local_filename, 'wb')
    file_size = int(r.headers['Content-Length'])
    chunk = 1
    num_bars = file_size / chunk
    bar =  progressbar.ProgressBar(maxval=num_bars).start()
    i = 0
    for chunk in r.iter_content():
        f.write(chunk)
        bar.update(i)
        i+=1
    f.close()
    return


def file_avail(url):
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False





# download_file(url)

def lfy():
    global year
    global month
    global mag
    global urlb
    for countyear in xrange(17):
        year = year + 1
        print "year is ", year
        if  year > 2002 and year < 2004:
            for countfirst in xrange(11):
                mag = mag + 1
                print mag
                month = month + 1
                print "month is", month
                urla = string1 + string2 + str(mag) + "/" 
                if month > 9:
                    urlb = string3 + "-" + str(mag) + "-" + str(year) + "-" + str(month)
                else:
                    urlb = string3 + "-" + str(mag) + "-" + str(year) + "-" + "0" + str(month)
                filetype = ".pdf"
                url = urla + urlb + filetype 
                decision = file_avail(url)
                if decision == True:
                    download_file(url)
                else:
	            continue
        else:
            month = 0
            for countmonth in xrange(12):
                mag = mag + 1
                print mag
                month = month + 1
                print "month is ", month
                urla = string1 + string2 + str(mag) + "/" 
                if month > 9:
                    urlb = string3 + "-" + str(mag) + "-" + str(year) + "-" + str(month)
                else:
                    urlb = string3 + "-" + str(mag) + "-" + str(year) + "-" + "0" + str(month)
                filetype = ".pdf"
                url = urla + urlb + filetype 
                decision = file_avail(url)
                if decision == True:
                    download_file(url)
                else:
	            continue
                
lfy()
                      
        
	




