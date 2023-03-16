from test2 import Child
class Parent:
    def parent_name(self):
        print("Palani and Uma")

    def some_method(self,entry):
        print(entry.child_name())

obj = Child()
m = Parent()
m.parent_name()
m.some_method(obj)