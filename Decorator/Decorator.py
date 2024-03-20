def decorator_function(original_function):
    def wrapper_function():
        print("Hello")
        return original_function()
        print("End")
    return wrapper_function

def display():
    print("Display function ran")

decorator_returned_value_only_memory = decorator_function(display)

decorator_returned_value_only_memory() # Calling the memory and executing the function

########################################################

