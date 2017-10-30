from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links = set()

def getLinks(pageUrl):
    global links
    html = urlopen("싸이트명" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    for link in bsObj.find_all('a', href=re.compile("^(/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in links:
                newPage = link.attrs['href']
                print(newPage)
                links.add(link.attrs['href'])
                if "pdf" in newPage:
                    pass
                elif "mp4" in newPage:
                    pass
                else:
                    getLinks(newPage)

getLinks("")
print(sorted(links))
