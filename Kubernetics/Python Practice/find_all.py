import requests
import bs4

url=requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
soap=bs4.BeautifulSoup(url.text,'lxml')

for i in soap.find_all('a'):
    if 'href' in i.attrs:
        print(i.attrs['href'])