# *args reprasent the tuples where **keyargs represent to dictonary

#example 1 *args

def my_list(a,b,c):
    return sum((a,b,c))

num=my_list(10,20,30)
print("the sum of my list 10,20 and 30 is {}".format(num))

#if i ll pass more argument in calling function like my_list(10,30,40,50) it will throe error as function can hold only three argumnets 
#for over come above situation i ll use *args

def my_list_args(*args):
    return sum(args)

num=my_list_args(10,30,40,100)
print("sum is {}".format(num))

#example 2 **kwargs

def my_grocery(veg):
    if veg == "onion":
        print("its vegitable")
        return veg
a=my_grocery("onion")
print(f"My veggie is {a}")


def my_grocery_fruit(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('true')
        print("my fev fruit is {} ".format(kwargs['fruit']))

my_grocery_fruit(fruit='Mango')
