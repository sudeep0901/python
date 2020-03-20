from urllib.parse import urlencode, urldefrag, quote, unquote 
import requests
# from requests.urllib3 import urlretrieve
import urllib
from urllib.request import urlretrieve


mydict = {
    "Name": "test name",
    "address": "test address",
    "fav char": "Shri Krishna"
}


strUrl = urlencode(mydict)
print(strUrl)

string = urlencode({"v": "what is your favroute editor, VS Code, atom , sublime"})
print(string)

sdecode = urldefrag(string)
print(sdecode)

qt = quote('Famous Quote:"I think, there I am')
print(qt)

print(unquote(qt))


fd = urllib.request.urlopen("ftp://ftp.oreilly.com")

print(fd.read())

fd.close()
ob = urlretrieve("ftp://ftp.oreilly.com", "menu.txt")
print(ob)

"""
retrieve.py example
"""


def callback(blocknum, blocksize, totalsize):
    print("Downloaded " + str((blocknum * blocksize)))
    print(" of ", totalsize)

urlretrieve("http://www.example.com/pyxml.xml", "px.xml", callback)
print("Download Complete")