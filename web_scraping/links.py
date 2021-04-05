 # Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page


import requests
import bs4

result=requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
sop=bs4.BeautifulSoup(result.text,'lxml')
#print(sop)
data=sop.select('.mw-redirect')
#print(data)

links=[]
book_title=[]

t=data.select('a')[1]['title']

print(t)
