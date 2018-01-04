import progressbar
import requests

url = "https://archive.org/download/Linux-For-You-Issue-78/Linux-\
For-You-78-2009-07.pdf"


def download_file(url):
    local_filename = 'lfy.pdf'
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

download_file(url)
