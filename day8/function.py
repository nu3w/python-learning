# function: like variable but in function bulk of code is defined in a function
# reusable, remove duplicate code

# syntax:
# def function_name():
#     statements
# function_name()   #function call

# requirement:
# create a function that prints out the intro of the user
# arguments: data sent during function call
# parameter: variable defined when function definition to accept the arguments

# def intro(name):
#     print(f'i am {name}')
# user = 'stela'
# intro(user)

# *****positional argument*****

def intro (name, age):
    print(f'''
name: {name}
age: {age}
''')
    
intro('stacy', 24)

# *****keyword argument*****

def intro2(name, age, address):
    print(f'''name = {name}
age = {age}
address = {address}''')
    
intro2(age = 20, address = "ktm", name = "hari")

# *****default argument*****

def intro3(name='default_name', age='default_age', address='default_address'):      # prints default value when no arguments are sent
    print(f'''name = {name}
age = {age}
address = {address}''')
    
intro3()

# todo:
# create a function that adds two numbers given by user
# get two numbers from user

def add(a, b):
    print('the sum of a and b is', a + b)

a = int(input('enter first number: '))
b = int(input('enter second number: '))    
add(a, b)

# implement function in calculator, task of for and while loop

def calculator():
    while True:  # runs until user exits
        print("\n--- Calculator Session ---")
        
        for i in range(2):  # allow 2 calculations per session
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")

            if op == '+':
                print("Result:", num1 + num2)
            elif op == '-':
                print("Result:", num1 - num2)
            elif op == '*':
                print("Result:", num1 * num2)
            elif op == '/':
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Cannot divide by zero")
            else:
                print("Invalid operator")

        choice = input("Do you want another session? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
        
calculator()