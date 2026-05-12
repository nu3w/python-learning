# file handling: read, write, edit

# open a file
# f = open('path_of_the_file', 'mode')
# f.close()

# file read('r)
f = open('file.txt', 'r')
a = f.read()
f.close()

print(a)

# file write('w'): overwrite: remove previous data, add new data, if the file doesnt exist, it creates a new one
f = open('file.txt', 'w')
b = f.write('a')
f.close()

print(b)

# file append mode('a'):  if the file doesnot exist, create new file, add new data along with old data
f = open('file.txt', 'a')
c = f.write(' c')
f.close()

# Accounting Program
# login or register
# if register: get user's username and password, store the data in file(user detail)
# if login: get user's username and password
# check if the username and password exists and correct by reading the file
# if yes: print login success,  give 3 option: 1. View balance 2. Add balance 3. Withdraw balance
#     if choice is 1: show the inital balance by reading the file(balance detail)
#     if choice is 2: get the amount to add from user, add the amount with initial balace and store it in the file(balance detail) and print
#     if choice is 3: get the amount to withdraw from user, compare the amount and initial balance by reading the file(balance detail), if amount is less than inital balance subtract amount from inital balace if amount is greateer than inital balance print out a statement that states the balanace is not enough
#     else
# exception handling
# function based