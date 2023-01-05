class Person:
    # Class attribute
    name1 = 'palani'

    @staticmethod
    def access1():
        return "Hello"

obj = Person()
#To call a static method, you use this syntax:
#className.static_method_name()
Person.access1()
# Static method cannot access class attribute name1 above