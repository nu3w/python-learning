# oop: object oriented programming

# class: structure, blueprints
# object: data created using class
# attributes: variables defined inside the class
# methods: a function defined inside a 
# 

# class class_name:
#     structures

# name = "ram"        # name --> variable

# class Student:
#     name = None        # name --> attribute
#     grade = None
#     address = None
#     phone = None
    
#     def show_detail(self):
#         print(f"""name: {self.name}
# address: {self.address}
# phone: {self.phone}
# grade: {self.grade}""")
        
#     def get_detail(self, name, address, phone):
#         self.name = name
#         self.address = address
#         self.phone = phone
        
#         self.show_detail()
        
# s1 = Student()
# s1.get_detail("sam", "ktm", "8796669786")
# s1.show_detail()
    
# s1 = Student()      # s1 is an object
# print(s1.name)
# print(s1.address)
# s1.gender = "male"
# print(s1.gender)
# s1.show_detail()

# create a animal class with attributes: name, eye, ear, legs and methods: get_detail, show_detail
# create 3 objects
class Animal:
    name = None
    eye = None
    ear = None
    legs = None
    
    def get_detail(self, name, eye, ear, legs):
        self.name = name
        self.eye = eye
        self.ear = ear
        self.legs = legs
        
    def show_detail(self):
        print(f"""name: {self.name}
eye: {self.eye}
ear: {self.ear}
legs: {self.legs}""")
        
a1 = Animal()
a1.get_detail("dog", 2, 2, 4)
a1.show_detail()

a2 = Animal()
a2.get_detail("cat", 2, 2, 4)
a2.show_detail()

a3 = Animal()
a3.get_detail("penguin", 2, "not visible", 2)
a3.show_detail()

# create a car class with attributes: model, brand, color,... and methods: get_detail, show_detail,
# create 2 objects
class Car:
    model = None
    brand = None
    color = None
    
    def get_detail(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        
    def show_detail(self):
        print(f"""model: {self.model}
brand: {self.brand}
color: {self.color}""")
        
c1 = Car()
c1.get_detail("civic", "honda", "red")
c1.show_detail()

c2 = Car()
c2.get_detail("model s", "tesla", "black")
c2.show_detail()