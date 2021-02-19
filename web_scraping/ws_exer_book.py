#here we will use the demo website https://books.toscrape.com/catalogue/page-2.html

import requests
import bs4

#base_url='https://books.toscrape.com/catalogue/page-2.html' 

# if i dont know which part i have to go then i can use teh {}

page=input('enter the page number')

base_url='https://books.toscrape.com/catalogue/page-{}.html'.format(page)

#print(base_url)

req=requests.get(base_url)

soup=bs4.BeautifulSoup(req.text,'lxml')

#print(soup)

obj=soup.select('.product_pod')[0]

print(obj)

print(len(obj)) #it will give the length of the pages

rating=obj.select(".star-rating.Three")

print(rating)

title=obj.select('a')[1]['title']

print(title)
