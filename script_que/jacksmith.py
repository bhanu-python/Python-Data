#if the sum of list <=21 then return sum if not reduce 10 if still not then print bust

def check_sum(mylist):
    if sum(mylist) <= 21:
        return sum(mylist)
    elif sum(mylist) > 21:
        a=sum(mylist)-10
        if(a <=21):
            return a
        else:
            print(' Bust ! ')


a=[1,2,3,20]
b=check_sum(a)
print(f"sum of my list is : {b}")
