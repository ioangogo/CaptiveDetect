#Libarys and global strings
import hashlib
import urllib
import logging
import webbrowser
from time import sleep
global md5ofs
global site
md5ofs = "4589f42e1546aa47ca181e5d949d310b"
site = "http://start.ubuntu.com/connectivity-check"
#The main part of the tester

def openbrowser():
    os=os.name
    if os=nt:
        #Test for browsers and launch
def hashcon(sitecon):
    #This part hashes the content of the website that urllib has just downloaded
    m = hashlib.md5()
    m.update(sitecon)
    res = m.hexdigest()
    return res
def getsite():
    r = urllib.urlopen(site)
    return r.read()
def checknetwork():
    hash = hashcon(getsite())
    if str(hash) == md5ofs:
        print "[INFO] No captive portal, site currently has md5 of ", hash
    else:
        print "[INFO] Captive portal detected, launching Browser Site MD5 hash", hash
        webbrowser.open("http://google.com") # opens the users defult Browser will remain google until I find out how to detect if the Captive portal redirects or takes over
def main():
    while True:
        checknetwork()
    time(10)
if __name__ == '__main__':
    main()
