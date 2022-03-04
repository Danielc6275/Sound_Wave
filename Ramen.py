from logging import NullHandler
import requests #getting TED talk page content

from bs4 import BeautifulSoup#web scraping

import re #Regular Expression pattern matching
# from urllib.request import urlretrieve #downloading mp4
import sys #for parsing args

#Exceptions Handlings

if len(sys.argv) > 1:
    url = sys.argv[1] #takes first argument passed thru
else:
    sys.exit("Get your UGLY, YELLAH, NO GOOD KEISTER OFF MY DOORSTEP")

#url = "https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"
r = requests.get(url) #stores content of object in variable r
print("Download is starting YA FILTHY ANIMAL")

soup = BeautifulSoup(r.content, features="lxml")
result = ""
for val in soup.findAll("script"):
    if(re.search("talkPage.init" , str(val))) is not None:
        result=str(val)

mp4_totals = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
#searches for proper url

mp4_url = mp4_totals.split('"')[0]#first output after split as mp4 url

print("Videos coming your way......" + mp4_url)
named_file = mp4_url.split("/") [len(mp4_url.split("/"))-1].split('?')[0]
print("Storing video...." + named_file)

r = requests.get(mp4_url) #extracts url content by getting requests
with open(named_file, 'wb') as f:
    f.write(r.content)

print("Process done YA FILTHy ANIMAL") 
#cli tool   