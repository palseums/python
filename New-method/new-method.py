class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 2)




x = SquareNumber(3)
print(x)  # 9
#######################

class Person:
    def __new__(cls, first_name, last_name):
        # create a new object
        obj = super().__new__(cls)

        # initialize attributes
        obj.first_name = first_name
        obj.last_name = last_name

        # inject new attribute
        obj.full_name = f'{first_name} {last_name}'
        return obj


person = Person('John', 'Doe')
print(person.full_name)

print(person.__dict__)



