# encapsulation: code single unit bind, data hiding: direct access of data through object is restricted
# make attributes and methods private (__) followed by att. and methods name
# to access 

class Login:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        
    def __show_detail(self):
        print(f"""email: {self.__email} 
password: {self.__password}""")
        
    def display(self):
        self.__show_detail()
        
l1 = Login("user", "pass")
l1.display()

# l1.show_detail()
# print(l1.__email)

# Bank class create
# bank_acc and back_balance attribute
# method: show detail
# bank_acc, bank_balance must not be directly accessable by object

class Bank:
    def __init__(self, bank_acc, bank_balance):
        self.__bank_acc = bank_acc
        self.__bank_balance = bank_balance
        
    def show_detail(self):
        print(f"""bank_ac: {self.__bank_acc}
bank_balance: {self.__bank_balance}""")
        
    def display(self):
        self.show_detail()
        
b1 = Bank(1234, 5000)
b1.display()