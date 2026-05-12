# inheritance: child/ derived and parent/ base class concept
# lets child class reuse the properties and behavior of another class(parent/ base class)

class Car:
    brand: None
    model: None
    color: None
    
    def get_detail(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        
    def show_detail(self):
        print(f"""brand: {self.brand}
model: {self.model}
color: {self.color}""")
    
class EV(Car):      # EV is child class and Car is parent class
    battery = None
    
    def get_info(self, battery):
        self.battery = battery
        
    def show(self):
        print(f"""brand: {self.brand}
model: {self.model}
color: {self.color}
battery: {self.battery}""")
        
    def charge(self):
        print(f"{self.brand} {self.model} is charging")

ev1 = EV()
ev1.get_detail("tesla", "model", "black")
ev1.get_info("70 kwh")
ev1.show()
ev1.charge()

# create a Animal class with attributes: eye, ear, legs and methods: get_detail, show_detail
# create dog class that inherits Animal class: add name att, movement(), get_name(), show_detail override
# create cat class that inherits Animal class: add name att, sound(), get_name(),show_detail override
# create 2 objects of dog
# create 2 objects of cat

class Animal:
    def __init__(self, eye, ear, legs):
        self.eye = eye
        self.ear = ear
        self.legs = legs
    
    def get_detail(self):
        return self.eye, self.ear, self.legs
        
    def show_detail(self):
        print(f"""eye: {self.eye}
ear: {self.ear}
legs: {self.legs}""")
        
class Dog(Animal):
    def __init__(self, eye, ear, legs, name):
        super().__init__(eye, ear, legs)
        self.name = name
        
    def movement(self):
        print(f"{self.name} is running")
        
    def get_name(self):
        return self.name
    
    def show_detail(self):
        print(f"dog name: {self.name}")
        super().show_detail()
        
class Cat(Animal):
    def __init__(self, eye, ear, legs, name):
        super().__init__(eye, ear, legs)
        self.name = name
        
    def sound(self):
        print(f"{self.name} says meow")
        
    def get_name(self):
        return self.name
    
    def show_detail(self):
        print(f"cat name: {self.name}")
        super().show_detail()
        
dog1 = Dog(2, 2, 4, "rocky")
dog2 = Dog(2, 2, 4, "tommy")

cat1 = Cat(2, 2, 4, "kitty")
cat2 = Cat(2, 2, 4, "moon")

dog1.show_detail()
dog1.movement()

dog2.show_detail()
dog2.movement()

cat1.show_detail()
cat1.sound()

cat2.show_detail()
cat2.sound()

# create Employee class
# attributes & methods: name, salary, show_detail()
# create manager class extende Employee class
# attributes and method: department, show_manager_detail()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show_detail(self):
        print(f"""name: {self.name} 
salary: {self.salary}""")
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def show_manager_detail(self):
        print(f"""name: {self.name}
salary: {self.salary}
department: {self.department}""")
        
e1 = Employee("ram", 2000)
e1.show_detail()

m1 = Manager("shyam", 5000, "IT")
m1.show_manager_detail()
m2 = Manager("sita", 5000, "HR")
m2.show_manager_detail()