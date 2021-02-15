# \d -> Numerix pattern
# \w -> alphanumeric patter along with some special charecter
# \D -> a non digit
# \s -> white space
# \W -> Non-Alphanumeric -> Specal Charcter
# \S -> non white space

import re

text="My number is 91-805-000-6621 and My mother number is 91-963-474-5439 "
op=re.search('\d\d-\d\d\d-\d\d\d-\d\d\d\d',text)
print(op)

#with Quantifier

op=re.search('\d{2}-\d{3}-\d{3}-\d{4}',text)
print(op)

#group the multiple match pattern

pat=re.compile(r'(\d{2})-(\d{3})-(\d{3})-(\d{4})')
op=re.search(pat,text)
print(op.group())

#if we want by indexing

print(op.group(1))


