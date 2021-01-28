# createing tic tac toe 

#asking the user choice

import subprocess

def user_choice():
    choice='false'
    choice_range=range(0,9)
    acceptable=False

    while choice.isdigit() == False or acceptable== False:
        
        choice=input('Please enter the position: ')
        
        if choice.isdigit()== False:
            print("Enter Valid Input !")

        if choice.isdigit()==True:
            if int(choice) in choice_range:
                acceptable=True
            else:
                print("Input valid poition")
                

    return int(choice)

     
#display the position

def display():

    tic=['0','1','2']
    tac=['3','4','5']
    toe=['6','7','8']

    for i in range(0,10):

        print(tic)
        print(tac)
        print(toe)
        
        position=user_choice()
        signe=xo_signe()
        
        if position in range(0,3):
            tic[position]=signe
        elif position in range(3,6):
            tacpos=position-3
            tac[tacpos]=signe
        else:
            toepos=position-6
            toe[toepos]=signe
        subprocess.run(['clear'])   #it will clear the prvious screen each time

#user ither can select X or Y

def xo_signe():
    signe_xo=input("enter the signe : ")
    return signe_xo

display()


