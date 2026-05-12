# identity operator: True, if both data and memory location is same, else, True

a = 10
b = 10
c = 15

# is:
print(a is b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))

# is not: True, if both data and memory locations are different, else, False
print(a is not b)
print(a is not c)