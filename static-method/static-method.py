class Person:
    # Class attribute
    name1 = 'palani'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def access1():
        return "Hello"

obj = Person()
#To call a static method, you use this syntax:
#className.static_method_name()
Person.access1()
# Static method cannot access class attribute name1 above
# Static method cannot access instance attribute name and age
