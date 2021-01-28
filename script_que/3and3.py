#this progam should return trur if there is 3 prasent next to a three

def three_guess(a):
    flag=0
    for i in a:
        if i == 3:
          flag += 1
          if flag==2:
              print("consucative 3 found")
              break
        else:
            flag=0
            

my_list=[1,2,3,4,5,3]
three_guess(my_list)
