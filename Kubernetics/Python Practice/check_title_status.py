import requests
import bs4

def url_status(url):
    try:
        status=requests.get(url)

        if '200' in str(status):
            soup=bs4.BeautifulSoup(status.text,'lxml')
            check=soup.select('title')
            if 'title' in str(check):
                print(check)
            else:
                print("title isnt avilable")
    except:
        print("input correct url or check connection")
    

url=input("enter the url : ")
url_status(url)

