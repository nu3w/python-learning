# membership operator: checks if a data exists in a sequencial data (string, list, tuple)

a = 'mindrisers'
b = [0, 2, 3, 6]

# in: True, if data exists, else, False 
print('z' in a)     # false
print('r' in a)     # true

#not in
print('z' not in a)     # true
print('m' not in a)     # false

# todo
# create a list of username
li = ['stella', 'stacy', 'john', 'jin']
# check if a name exists in the list
print('stella' in li)       # true

a = [1, 2, 3, 4]
b = [1, 2, 3]
# check if b exists in a
print(b in a)       # false

x = [1, 2, 3]
y = [1, 2 ,3]
# check if x exists in y
print(y in x)       # false