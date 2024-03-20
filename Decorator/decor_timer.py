def my_timer(original_function):
    import time
    def wrapper_function(*args,**kwargs):
        t1 = time.time()
        original_function(*args,**kwargs)
        t2 = time.time() - t1
        print(f"The time taken to run this function {original_function.__name__} is {t2}")
    return wrapper_function

@my_timer
def display_info(name,age):
    print(f"You have executed is {name},{age}")


display_info("palani",42)

