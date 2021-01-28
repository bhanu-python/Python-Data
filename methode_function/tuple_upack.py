#unpacking tuples
#pass the employe name and total work of mins calculate who worked for most hours

office=[('Bhanu',700),('Ravi',400),('Sia',650)]

def unpack_tup(val):
    wh=0
    name=''
    for i,j in val:
        temp=j/60
        if temp > wh:
            wh=temp
            name=i
        else:
            pass
    return(name,wh)

a=unpack_tup(office)
print(a)     
