def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print('Logging exception:', str(ex))
        raise

When handling an exception, you may want to raise another exception. For example:

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError('b must not zero')