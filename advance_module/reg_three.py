# Or Opretor '|'

import re

#if I want to search any of one charecter

print(re.search(r'cat|dog','Colour of my cat is black'))

print(re.search(r'cat|dog','Colour of my dog is black'))

#in below case it will take the first match

print(re.search(r'cat|dog','Colour of my cat and dog is black'))

# 2 -> Wild card charecter '.'

#below will find the at avaialble in string if i want complete one

print(re.findall(r'at','My cat , sat on a table lat'))

#using wild card charecter -> below will take extra char before the at

print(re.findall(r'.at','My cat , sat on a table lat'))

# i can use n number ogf wild card charecter -> wild card contain cany charecter including space

print(re.findall(r'...at','My cat , sat on a table splat'))


#if i want to igonre somthing in a string and print other

print(re.findall(r'[^\d]','My Number range is 1 to 21'))

#it will append the char occurance and ingnore the digit

print(re.findall(r'[^\d]+','My Number range is 1 to 21'))

#or with substr

print(re.findall(r'cat(fish|alina|apiller)','I am having a catfish,catalina,catapiller'))
