from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup

import csv
 
try:
 
    html = urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm")
 
except HTTPError as e:
 
    print(e)
 
except URLError:
 
    print("Server down or incorrect domain")
 
else:
 
    res = BeautifulSoup(html.read(),"html5lib")
 
    tags = res.findAll(class_=["tbody", "td", "B3"])
 
    for tag in tags:
 
        print(tag.getText())

    tagss = res.findAll(class_=["tbody", "td", "B6"])
 
    for tag in tagss:
 
        print(tag.getText())
