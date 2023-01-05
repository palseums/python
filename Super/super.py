class Base(object):

	# Constructor
	def __init__(self):
		self.name = "Palani"

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

	# Constructor
	def __init__(self):
		self.age = 15
		super().__init__()

	# To get name
	def getAge(self):
		return self.age

obj = Child()
print(obj.getName(