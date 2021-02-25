s={1,2,3,4}
sc=s.copy()  # it will copy the set s to sc
s.add(5)
print(s.difference(sc)) #this methode will give diffrance between sets

# below function compares the set and will remove the matching from set1

s1={1,3,5}
s2={1,4,6}

s1.difference_update(s2)
print(s1)

# below function remove the infor from set 

s.discard(2)
print(s)

s3={1,2,3,4}
s4={1,2,5,3}

print(s3.intersection(s4))

s3.intersection_update(s4)
print(s3)
