#dictonary comprihension 

print({x:x**3 for x in range(10)})

print({k:v**3 for (k,v) in zip(['a','b','c'],range(10))})
