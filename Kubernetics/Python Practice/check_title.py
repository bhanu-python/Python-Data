# Write a Python program to check whether a page contains a title or not.

import requests
import bs4

url="https://en.wikipedia.org/wiki/Wikipedia"
source=requests.get(url)
#print(source.text)
soup=bs4.BeautifulSoup(source.text,'lxml')
data= soup.select('title')
#print(data)
if 'title' in str(data):
    print(data)
else:
    print('title isnt available')