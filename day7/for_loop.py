# for loop:

# iterable: sequential datatype (string, group datatype)
a = [1, 2, 3, 4, 5]
# iteration: process of moving from first index of data to last index
# iterator: variable used to perform iteration in iterable

# for iteration in iterable:
#   statements

for i in a:
    print(f'hello, {i}')
    
# todo
# define a word/ list
# print out each character/ data
word = ('HELLO')
for i in word:
    print(i)

# define a list of username
# get a username from user
# check if it exists in the list
username = ['ram', 'sita']
get = input('enter username: ')
found = False
for user in username:
    if user == get:
        found = True
        break
    
if found:
    print('username exists')
else:
    print('username not found')

# define a dictionary with username as key and password as value
# get username and password from user
# check if username exists in the dictionary and the password matches
di = {
    'ram':'1234',
    'sita':'4321'
}
username = input('enter username: ')
password = input('enter password: ')
found = False
for user, pw in di.items():
    if user == username and pw == password:
        found = True
        break
    
if found:
    print('login successful')
else:
    print('invalid username or password')