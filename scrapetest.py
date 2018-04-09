from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(),"lxml")
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print('Title could not be found')
else:
    print(title)

