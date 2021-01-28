num=int(input("entert the number: "))
numc=num
l=len(str(num))
print('length of the number{}'.format(l))
i=0
temp=0
while i < l:

    pal=num % 10
    temp=pal + temp*10
    num = int(num / 10)
    i += 1
if numc == temp:
    print(f'{numc} is Plaindrome {temp}')
else:
    print("{} is not palindrome {}".format(numc,temp))
    
