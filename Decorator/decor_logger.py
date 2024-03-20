def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)
    def wrapper_function(*args,**kwargs):
        logging.info(f"Ran with arguments args: {args},kwargs:{kwargs}")
        return original_function(*args,**kwargs)

    return wrapper_function

@my_logger
def display_info(name,age):
    print(f"Display function ran with{name} and {age}")


display_info("palani",42)