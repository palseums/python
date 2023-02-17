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