import requests
from bs4 import BeautifulSoup
import urllib
import sys
import os


url =  'https://'+ sys.argv[1]

try:
    os.makedirs('downloads')
except:
    pass


resource = urllib.urlopen(url)
content =  resource.read().decode("utf-8")

soup = BeautifulSoup(content, "html.parser")
for img in soup.findAll('img'):

     src = img.get('src')
     print(src)
     if src.split('/')[1] == 'images':
         src = url + src
     else:
         src = 'http:' + src
         urllib.urlretrieve(src,  'downloads/' + src.split('/')[-1])

for i in soup.findAll('link', type="text/css"):
    src = url + i.get('href').split('?')[0]
    urllib.urlretrieve(src, 'downloads/' + src.split('/')[-1])

for script in soup.findAll('script'):
     src = script.get('src')
     if src != None:
         if src.split('/')[0] != 'https:':
            src = url + src
         src = src.split('?')[0]
         urllib.urlretrieve(src, 'downloads/' + src.split('/')[-1])

