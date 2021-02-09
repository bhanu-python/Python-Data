# To check which line you are getting error and enableing the trace

import pdb

x=[1,2,3]
y=5
z=7

res1=y+z

pdb.set_trace() #in this line i am seeting the trace as i know i am getting error after that 

rest=y+x
