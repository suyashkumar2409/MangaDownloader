from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve,FancyURLopener
#from urllib import urlretrieve
import os,sys
#import urllib2


starting = "C:/"
def makeDirectory(path):
    if not os.path.exists(path):
            os.mkdir(path)

def findLastPage(selectPage):
    lastPage = 0
    for i in selectPage.find_all("option"):
        if lastPage < int(i.string):
            lastPage = int(i.string)

    return lastPage

def downloadPage(directory,link,name,chap):

    try:
        url = urlopen(link)
        readHtml = url.read()
        pageSoup = BeautifulSoup(readHtml,"html.parser")

        url.close()

        imglink = pageSoup.find("div",{"id":"imgholder"}).img['src']

        #urlretrieve(imglink,directory+"/"+str(name)+".jpg")

        class MyOpener(FancyURLopener):
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/2007127 Firefox/2.0.0.11'

        myopener = MyOpener()

        #downloadTo =
        #print("here")
        myopener.retrieve(imglink,directory+"/"+str(name)+".jpg")

    except: #all excp
        print(str(name)+" page of chapter "+str(chap)+ ' failed')

def downloadManga(manga,start,end):

    mangaPath = "C:/"+ manga
    makeDirectory(mangaPath)

    for chap in range(int(start),int(end+1)):
        try:
            url = urlopen("http://www.mangareader.net/"+manga+"/"+str(chap))
            readHtml = url.read()
            chapSoup = BeautifulSoup(readHtml,'html.parser')

            url.close()

            lastPage = findLastPage(chapSoup.find("div",{"id":"selectpage"}))

            currDirectory = mangaPath+"/"+str(chap)
            makeDirectory(currDirectory)

            for i in range(1,int(lastPage)+1):
                imglink = "http://www.mangareader.net/"+manga+"/"+str(chap)+"/"+str(i)
                downloadPage(currDirectory,imglink,i, chap)

            print("Chapter "+str(chap)+" of "+str(manga)+" has been downloaded.")

        except:
            print("Chapter "+str(chap)+" link is not opening")





manga = input("Write the name of the manga you want")

start = input("Which chapter should it start from?")

end = input("Which chapter should it end to?")
downloadManga(manga,int(start),int(end))