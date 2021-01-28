def hello(naam='Bhanu'):
    print("I am inside hello function")

    def hi():
        print("\t I am inside the hi function")

    def name():
        print('\t I am inside name function')
    
    #we can call the below function withing the scope of hello function cant be call by out side
    
    #--> hi()
    #--> name()
    
    #beow we are trurning the function name
    if naam == 'Bhanu':
        return name
    else:
        return hi

a=hello('Bhanu')

print(a)

a()
