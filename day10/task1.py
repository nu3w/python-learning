# Accounting Program
# create a dictionary with username as key and password as value
# create a dictioanry with username as key and intial_balance as value
# get user's username and password
# check if the username and password exists and correct
# if yes: print login success,  give 2 option: 1. View balance 2. Add balance 3. Withdraw balance
#     if choice is 1: show the inital balance
#     if choice is 2: get the amount to add from user, add the amount with initial balace and print
#     if choice is 3: get the amount to withdraw from user, compare the amount and initial balance, if amount is less than inital balance subtract amount from inital balace if amount is greateer than inital balance print out a statement that states the balanace is not enough
#     else
# exception handling
# function based

userlogin = {'ram':'ram1', 'sita':'sita2', 'laxman':'laxman3'}
userblc = {'ram': 2000, 'sita': 1500, 'laxman': 500}

def firstchoice(username):
    print('balance: ', userblc[username])
        
def secondchoice(username):
    try:
        deposit = int(input('enter deposit amount: '))
        if deposit <= 0:
            print('amount must be positive')
            return
        userblc[username] += deposit
        print('updated balance: ', userblc[username])
    except ValueError:
        print('invalid input')
        
def thirdchoice(username):
    try:
        withdraw = int(input('enter withdraw amount: '))
        if withdraw <= 0:
            print('amount must be positive')
            return
        if withdraw > userblc[username]:
            print('insufficient balance')
            return
        userblc[username] -= withdraw
        print('updated balance: ', userblc[username])
    except ValueError:
        print('invalid input')
    
while True:
    username = input('enter your username: ')
    password = input('enter your password: ')
        
    if username in userlogin and userlogin[username] == password:
        print('login successful')
            
        while True:
            try:
                choice = int(input('1: view balance, 2: deposit, 3: withdraw, 4: logout: '))
                    
                if choice == 1:
                    firstchoice(username)
                elif choice == 2:
                    secondchoice(username)
                elif choice == 3:
                    thirdchoice(username)
                elif choice == 4:
                    print('logged out')
                    break
                else:
                    print('enter a number from 1 - 4')
                        
            except ValueError:
                print('invalid input')
                    
    else: 
        print('invalid username or password')
                
    # repeat = input('do you want to continue?(y/n): ')
    # if repeat.lower() != 'y':
    #     break