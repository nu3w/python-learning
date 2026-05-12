# polymorphism: poly -> multiple, morph -> form
# different class have method with same name
# methods depend on the objects

# a = 10
# b = 5
# print(type(a))

# x = "the"
# y = " mindrisers"

# print(a.__add__(b))       # (a + b)
# print(x.__add__(y))       # (x + y)

class int:
    def __add__(self):
        print("add two numbers")
        
class str:
    def __add__(self):
        print("join two strings")

class Dog:
    def move(self):
        print("walk")
        
class Bird:
    def move(self):
        print("fly")
        
class Fish:
    def move(self):
        print("swim")
        
d1 = Dog()
b1 = Bird()
f1 = Fish()

d1.move()
b1.move()
f1.move()