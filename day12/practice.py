# while True:
#     userlogin = {'ram':'ram1', 'sita':'sita2', 'laxman':'laxman3'}
#     userblc = {'ram': 2000, 'sita': 1500, 'laxman': 500}

#     username = input('enter your username: ')
#     password = input('enter your password: ')

#     if username in userlogin and userlogin[username] == password:
#         choice = int(input('press 1 to check balance, 2 to deposit and 3 to withdraw: '))
#         if choice == 1:
#             print(userblc[username])
#         elif choice == 2: 
#             deposit = int(input('enter deposit amount: '))
#             userblc[username] += deposit
#             print('your new balance: ', userblc[username])
#         elif choice == 3:
#             withdraw = int(input('enter withdraw amount: '))
#             if userblc[username] < withdraw:
#                 print('insufficient balance')
#             else:
#                 userblc[username] -= withdraw
#                 print('your new balance: ', userblc[username])
#         else:
#             print('please enter number from 1 - 3')
#     else:
#         print('invalid username or password')
        
#     choice = input('would you like to continue?(y/n): ')
#     if choice != 'y':
#         break

import json

file_name = "data.json"


def load_data():
    try:
        with open(file_name, "r") as f:
            return json.load(f)         # converts json file into python dictionary
    except:
        return {}       
    
def save_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)        # converts dictionary to json format and save
        

def  register():
    data = load_data()      # load existing users from file
    
    username = input("enter username: ")  
    
    if username in data:
        print("username already exists")
        return
    
    password = input('enter password: ')
    
    data[username] = {
        "password": password,
        "balance": 0.0
    }
    
    save_data(data)
    print("registration successful")
    
def login():
    data = load_data()
    
    username = input('enter username: ')
    password = input("enter password: ")
    
    if username in data and data[username]["password"] == password:
        print('login successful')
        return username
    else:
        print("invalid credentials")
        return None
    
    
def view_balance(username):
    data = load_data()
    
    print("your balance: ", data[username]["balance"])

def deposit_balance(username):
    try:
        amount = float(input('enter amount to deposit: '))
        data = load_data()
        
        data[username]["balance"] += amount
        save_data(data)
        
        print("balance deposited successfully")
    except:
        print("invalid input")
        
def withdraw_balance(username):
    try:
        amount = float(input("enter amount to withdraw: "))
        data = load_data()
        
        if amount > data[username]["balance"]:
            print("insufficient balance")
        else:
            data[username]["balance"] -= amount
            save_data(data)
            print("withdrawal successful")
    except:
        print("invalid input")
        
        
def user_menu(username):
    while True:
        print("\n1. view balance")
        print("2. deposit balance")
        print("3. withdraw balance")
        print("4. logout")
        
        choice = int(input("enter your choice: "))
        
        if choice == 1:
            view_balance(username)
        elif choice == 2:
            deposit_balance(username)
        elif choice == 3:
            withdraw_balance(username)
        elif choice == 4:
            break
        else:
            print("invalid choice")
            

def main():
    while True:
        print("\n1. register")
        print("2. login")
        print("3. exit")
        
        choice = int(input("enter your choice: "))
        
        if choice == 1:
            register()
        elif choice == 2:
            user = login()
            
            if user:
                user_menu(user)
        elif choice == 3:
            print("goodbye")
            break
        else:
            print("invalid choice")
            
            
if __name__ == "__main__":
    main()