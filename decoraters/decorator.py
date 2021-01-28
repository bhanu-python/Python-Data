def new_decorator(orignal_func):
    print("New decorator")
    def wrap_func():
        print("\t Wrap function")
        orignal_func()
        print("\t back to wrap function")
    
    return wrap_func

@new_decorator
def decorator_func():
    print("orignal decorator")

#to over come the below function calling we will use the @
#test=new_decorator(decorator_func)
#test()

decorator_func()
