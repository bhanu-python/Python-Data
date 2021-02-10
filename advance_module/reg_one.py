import re

    #above we imported reguler expression module

    #1 with in key word

a= 'Bhanu' in 'My name is Bhanu Pratap Mehta'

    #here "a" weill give you the booleann result wether its availale or not

print(a)

    #2 with module re

text='My name is bhanu, My Phone number is (+91)8050,006,621'

pattern='Phone'

print(re.search(pattern,text))

    #above search option will serach the pattern in vailable string will provide you the index value as well

    #if there is no pattern found it wont return any thing and its provide you the only forst match

    #if there are more than 1 matched pattern

text='Phone one,Phone two,Phone three'

pattern='Phone'

outp=re.findall(pattern,text)

    #above give you output all the mtached string as a list

print(outp)

    #if you want to combine seach and find all we can use below

for match in re.finditer(pattern,text):
    print(match) #it will give you all the matched attern and their indexes
