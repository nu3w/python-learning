# loop: execute a block of code multiple times

# while loop: condition
# while condition:
#   statement1
#   statement2

# if the condition is true, while block is executed, condition has to be changed to false to end the loop
# condition false -> block is not executed, while block exit

# a =  1
# b = 5
# while a < b:
#     a += 1
#     if a == 3:
#         break
#     print(a)
    
# break: terminated/ end the loop
# continue: current loop skip, and start new loop

# todo:
# Mark Evaluator (also implement while loop)
# ask user for exam mark
# if the mark is greater than or equal to 90 and less than 100: print a statment(eg. Excellent)
# if the mark is greater than or equal to 80 and less than 90: print a statment
# if the mark is greater than or equal to 70 and less than 80: print a statment
# if the mark is greater than or equal to 60 and less than 70: print a statment
# if the mark is greater than or equal to 50 and less than 60: print a statment
# if the mark is greater than or equal to 40 and less than 50: print a statment
# if the mart is less than 40 print a statment
# if the user input is negative or greater than 100: print a statement
while True:
    mark = int(input("Enter your exam mark (0–100): "))

    if mark < 0 or mark > 100:
        print("Invalid mark! Please enter between 0 and 100.")
    
    elif mark >= 90:
        print("Excellent")
    elif mark >= 80:
        print("Very Good")
    elif mark >= 70:
        print("Good")
    elif mark >= 60:
        print("Satisfactory")
    elif mark >= 50:
        print("Pass")
    elif mark >= 40:
        print("Below Average")
    else:
        print("Fail")

    choice = input("Do you want to check another mark? (yes/no): ")

    if choice != "yes":
        print("Program ended.")
        break

# ask user to enter a text,
text = input('write a message: ')
# ask user the number of times they want to print the text
repeat = int(input('enter the number of times you want to repeat the message: '))
# using while print out the text as the specified number
count = 0

while count < repeat:
    print(text)
    count += 1

# for loop: 