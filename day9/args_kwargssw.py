# args: * used to define args, enable a parameter to accept multiple arguments, data in tuple

def add(*args):
    total = 0
    for i in args:
        total += i
    print(total)
    
add(8,9,10)

# kwargs: ** used to define kwargs, enable paremeter to accept multiple keyword arguments, data in dictionary

def intro(**kwargs):
    print(kwargs.items())
    # print(kwargs.keys())
    # print(kwargs.values())
    for i, j in kwargs.items():
        print(f'{i} : {j}')
    
intro(name = 'sam', age = 23)

# return: function end, return the data from the function to the function call
# global variable: can be used anywhere, it is defined in a python file
# local variable: can only be used within that function, it is defined inside a function
x = 10      # global variable
def add(a, b):
    c = a + b       # local variable
    print('Inside Function')
    print(c)
    print(x)
    return c
d = add(3, 4)
print(d)
print('Outside Function')
print(x)
# print(c)        # is a local variable

y = 10
def add(z):
    global y
    y += z
    print(y)
add(10)
    
# decorator:
def greet(a):       # a = intro
    print('hello')
    a()     # intro()
    
    
@greet      # greet(intro)
def intro():
    print('i am sam')