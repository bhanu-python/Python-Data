
import csv
#remove duplicates from list

data=[]
def remove_duplicate(info):
    for dup in info:
        if dup in data:
            continue
        data.append(dup)
info=[1,2,2,3,3,3,4,4,4,4]
remove_duplicate(info)
print(data)

#remove duplicates from a csvfile and excel

fcsv= open('dupe.csv',mode="w+",newline="")

wcsv=csv.writer(fcsv,delimiter=",")

#for i in info:
wcsv.writerow(list(info))

fscv=open("dupe.csv",mode="r")
rcsv=csv.reader(fscv)

print(rcsv)
col=[]
for i in rcsv:
    col.append(i)

print(col)

