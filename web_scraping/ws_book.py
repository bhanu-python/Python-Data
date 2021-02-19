#USE THE url https://books.toscrape.com/catalogue/page-1.html AND GET ALL THE TWO STARS BOOK NAME

import requests
import bs4

two_star_book=[]
base_url='https://books.toscrape.com/catalogue/page-{}.html'

for page in range(1,21):
    
    base_url='https://books.toscrape.com/catalogue/page-{}.html'.format(page)
    books=requests.get(base_url)
    soup=bs4.BeautifulSoup(books.text,'lxml')
    product=soup.select('.product_pod')

    for book in product:

        if len(book.select('.star-rating.Two')) != 0:
            book_title=book.select('a')[1]['title']
            two_star_book.append(book_title)

for i in two_star_book:
    print(f' ** {i}')



