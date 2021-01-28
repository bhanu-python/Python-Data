from random import shuffle
my_list=[' ',0,' ']

shuffle(my_list)

print(my_list)

def user_guess():
    print("we are in fun 1")
    g=''
    
    while g not in ['0','1','2']:
        g=input("enter the position 0,1,2: ")

    return int(g)

def check_guess(my_list):
    print("we are fun 2")

    k=user_guess()
    for i in my_list:
        if my_list[k] == 0:
            print(" you found the ball")
            break
        else:
            print(' OOPS ! ')
            break

check_guess(my_list)





