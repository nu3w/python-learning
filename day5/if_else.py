# if else statement: multi lined statement, conditional statement
# if and elif block takes condition, else block doesn't
# if condition is true -> block execute, if condition is false -> next block condition is checked
# else block is executed when all conditions in upper blocks are false

# syntax :-
# if condition:
#   statement

# w = 'sunny'

# if w == 'raining':
#     print('take umbrella')
# elif w == 'cloudy':
#     print('it may rain, better take umbrella')
# else:
#     print('don\'t take umbrella')
    
# print('program end')

# a = 10
# b = 5

# if a < b:
#     print('a is less than b')
# elif a > b:
#     print('a is greater than b')
# elif a == b:
#     print('a and b are equal')
# else:
#     print('invalid')
    
# simple calculator
# define two variables and assign numbers to them
# define a variable(op) and assign a symbol(+,-,*,/)
# if op is +, add two numbers
# if op is -, subtract two numbers
# if op is *, multiply two numbers
# if op is /, divide two numbers

while True:
    a = int(input('enter first number: '))
    b = int(input('enter second number: '))

    op = input('Enter operation (+, -, *, /): ')

    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    else:
        print('invalid operator')
        
    choice = input('Do you want to continue? (yes/no): ')
    
    if choice == 'yes':
        continue
    elif choice == 'no':
        break

# calculator ma implement simple calculator  
# ask user if they want to end the calculation or not:
# if user input yes: end the program, if no: rerun the program