from collections import defaultdict

dec={1:"Bhanu",2:"Bhawana"}

print(dec[1])

#what if i ll print the key value which is not available

#print(dec[3]) #we will get a key errror 

#import defaultdictonary to over come of the aboave issue

dec=defaultdict(lambda:"N/A")

print(dec[3])
