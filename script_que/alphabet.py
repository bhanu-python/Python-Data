import string
al=input('enter the string:')
#alp=shuffle(al)
k=0
flag=0
for i in string.ascii_lowercase:
    for j in al.lower():
        #print(f'value of j: {j}')
        if  j != i:
            flag = 1
            continue
        else:
            flag = 2
            break
if flag == 1:
    print("all alphabet not available")

if flag == 2:
    print("all alphabet available")

    





            
