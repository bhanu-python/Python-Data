i=1
row=int(input("enter the number of rows : "))
while i <= row:
    j=1
    k=1
    temp= row - i
    while j <= temp:
        print(' ',end='')
        j += 1
    temp1= 2 * i - 1
    while k <= temp1:
        print('*',end='')
        k += 1
    i += 1
    print()

