import wget
global ds
ds = list()

class Dollect:
    def __init__(self, ds):
        self.ds = ds
      #  print ds
    global html
    for package in ds:
        print package
    html = "http://audio-video.gnu.org/video/rms-education-es-high-sub.en.ogv"
    def download(self,ds):
        for package in ds:
            print package
       # filename = wget.download(html)

arca = ['Cpio','Gzip','Paxutils','Sharutils','Tar','Xorriso']
dobject = Dollect(arca)
dobject.download(arca)
