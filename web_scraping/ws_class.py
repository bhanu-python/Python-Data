import requests
import bs4

rqst=requests.get('https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam')
soup=bs4.BeautifulSoup(rqst.text,'lxml')
item=soup.select('.toctext')[0]
print(item.text)


#if i want all the item

for item in soup.select('.toctext'):
    print(item.text)

