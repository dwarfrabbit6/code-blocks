#1st arg: class name(internal representation of the class), 2nd arg: any bases(anything you inherit from), 3rd arg: attributes & methods
newClass = type("Test",(),{})  #this line is equivalent to the 'Test' class above
print(Test)
print(type(Test))

print("\n")
class Greet:
	def greet(self):
		print("Hello")
