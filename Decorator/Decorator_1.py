def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("Hello")
        original_function(*args,**kwargs)
        print("End")
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")


@decorator_function
def display_info(name,age):
    print(f"Display function ran with {name},{age}")


display_info("palani",42)
display()




########################################################

