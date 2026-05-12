# exception handling:

# try-except
# try: include lines of code that raises exception
# except block is executed when exception is raised in try block

try:
    a = int(input('enter number: '))
    print(a + 10)
except: 
    print('enter integer')