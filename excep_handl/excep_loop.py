def in_num():
    while True:
        try:
            number=int(input("Enter a number : "))
        except:
            print("its not a number")
            continue
        else:
            print("its a number")
            break

in_num()
