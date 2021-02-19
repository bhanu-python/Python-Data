import requests
import bs4

req=requests.get('https://en.wikipedia.org/wiki/Sachin_Tendulkar')

##print(req.text.encode('utf-8'))

soup=bs4.BeautifulSoup(req.text,'lxml')

#iprint(soup.encode('utf-8'))

#print(soup.select('img')[0])

img=soup.select('.thumbimage')[0]

#img object can be use a dictonary

print(type(img))

print(img['src'])

res=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Anjali-Sachin.jpg/220px-Anjali-Sachin.jpg')

print(res.content) #as its a not text file so we have to use content

#now we have to save this file as image format

f=open('sachin.jpg','wb') # wb for the binary file as the content
f.write(res.content)
f.close()
