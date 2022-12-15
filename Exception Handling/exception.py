try:
    s = "palani"
    c = 10 / 0
# Exception Base class for all exception
except Exception as e:
    print(e)
else:
    print("else")
finally:
    print("finally")
# When there is error in try block except block will be executed else block will not execute
# When there is exception in try block Except block will be executed else block will not execute
# When there is no Error/ Exception in try block,Else block will be executed
# Finally block will always be executed
# To find all the python exception
# https://www.tutorialspoint.com/python/standard_exceptions.htm