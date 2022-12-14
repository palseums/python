def suma_func():
    print("Palani")

// How to define a class

class Dog():
    Dog_name = 'Rocky'
    def get_dog_name(self):
        print(self.Dog_name)

    def set_dog_name(self,dog_name):
        self.Dog_name = dog_name

    def set_other_variables(self,var1,var2):
        self.varr1 = var1
        self.varr2 = var2

    def get_other_variables(self):
        print(self.varr1)
        print(self.varr2)

    def __del__(self):
        print("Object got deleted")

// Write the below code in another file
// How to call a class in another file


import test2
c = test2.Dog()
c.get_dog_name()
test2.suma_func()



