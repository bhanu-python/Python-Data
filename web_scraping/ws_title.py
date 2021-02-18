#step 1

import requests

#step 2

import bs4

#1
#it will get all the source code of a website

rqst=requests.get('http://www.example.com')
# print(rqst.text) #--> uncomment the print check the source

#2
#will convert sorce code string to correct allignment or readable form

soup=bs4.BeautifulSoup(rqst.text,'lxml')

#print(soup)

#grab the tags details

#for exampe i want to grab the title tag

print(soup.select('title'))

#if i juct want the info doesnt wnat to include tag

print(soup.select('title')[0].getText())
