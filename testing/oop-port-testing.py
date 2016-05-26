import wget

class Dollect:
    global html
    global arca
    arca = list()
    html = "http://audio-video.gnu.org/video/rms-education-es-high-sub.en.ogv"
    arca = ['Cpio','Gzip','Paxutils','Sharutils','Tar','Xorriso']
    def download(self):
        for package in arca:
            print package
        filename = wget.download(html)

dobject = Dollect()
dobject.download()
