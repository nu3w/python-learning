# data types:

# string
# everything inside quotes(single ' ' or double " ") are considered string

# a = 'my name's john' #raises syntax error
a = 'my name\'s john'
b = "my name's john"
c = '''my name's john 
i am a "student"'''

print(a)
print(b)
print(c)
print('datatype of a is', type(a))

# integer: numbers
d = 1
print(d)
print(type(d))

# float: decimal numbers
e = 1.2
print(e)
print(type(e))

# boolean: true or false
f = True
g = False
print(g)
print(type(g))

# none: None
h = None
print(h)
print(type(h))

# group dataype
# list: [] is used to define a list, multiple datatypes can be included, ordered, mutable
my_list = ['a', 'b', 'c', 1, 2, 3]
print(my_list)
print(type(my_list))

# tuple: () is used to define a list, multiple datatypes, ordered, immutable
my_tup = ('a', 'b', 1, 2)
print(my_tup)
print(type(my_tup))

# set: {} is used to define a set, multiple datatypes, unordered, unique values 
my_set = {'a', 'b', 1, 2, 2} # does not take duplicate datas
print(my_set)
print(type(my_set))

# dictionary: {} is used to define key:value pairs, key must be unique
my_dict = {"fruit":"orange", "veggie":"cabbage"}
print(my_dict)
print(type(my_dict))