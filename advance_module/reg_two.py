# \d -> Numerix pattern
# \w -> alphanumeric patter along with some special charecter
# \D -> a non digit
# \s -> white space
# \W -> Non-Alphanumeric -> Specal Charcter
# \S -> non white space

import re

text="My number is 91-805-000-6621 "
op=re.search('\d\d-\d\d\d-\d\d\d-\d\d\d\d',text)
print(op)

#with Quantifier

op=re.search('\d{2}-\d{3}-\d{3}-\d{4}',text)
print(op)
