class Person:

    name1 = 'Palani'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi. I'm {self.first_name} {self.last_name}. I'm {self.age} years old."

    @classmethod
    def create_anonymous(cls):
        return Person('John', 'Doe', 25)
    @classmethod
    def access1(cls):
        return cls.name1

#The class method cannot access instance attributes. But it can access class attributes via the cls variable.
# To call a class method, you use the class name, followed by a dot, and then the method name like this
#ClassName.method_name()
c = Person.create_anonymous()
print(c.introduce())
print(c.name1)

