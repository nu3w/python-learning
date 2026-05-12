# Ecom CLI
# create a dictionary with username, password and usertype(buyer/seller)
# create a dictionary with product detail: name, description, price
# get user's username and password
# check if the username and password exists and correct and get the usertype from the dict of that user
# if yes: print login success
#     check the usertype:
#     if the usertype is buyer:
#       # show choices 1. view products 2. Buy Products: get what they want to buy and quantity: print total price price*quantity
#     if the usertype is seller:
#        # show choices 1. view my products 2. add products(product name, description, price) 
# if user doenot exist print a statement
# exception handling
# function based

u1 = {'username':'ram',
      'password': 'ram1',
      'usertype':'seller'}
u2 = {'username':'sita',
      'password': 'sita2',
      'usertype':'buyer'}
users = [u1, u2]

p1 = {'name':'product1',
      'description': 'this is product1',
      'price': 5}
p2 = {'name':'product2',
      'description': 'this is product2',
      'price': 15}
products = [p1, p2]

while True:
    username = input('enter username: ')
    password = input('enter password: ')

    found = False

    for user in users:
        if user['username'] == username and user['password'] == password:
            found = True
            print('login successful')
            
            if user['usertype'] == 'buyer':
                print('1. view products')
                print('2. buy products') 
                
                while True:
                    choice = int(input('enter your choice: '))
                    
                    if choice == 1:
                        for product in products:
                            print(f"name: {product['name']}, description: {product['description']}, price: {product['price']}")
                    
                    elif choice == 2:
                        product_name = input('enter product name: ')
                        quantity = int(input('enter quantity: '))
                        
                        found_product = False
                        
                        for product in products:
                            if product['name'] == product_name:
                                total_price = product['price'] * quantity
                                print('total price is ', total_price)
                                found_product = True
                                break
                            
                        if not found_product:
                            print('product not found')
                            
                    else:
                        print('please choose 1 or 2')
                        
            elif user['usertype'] == 'seller':
                print('1. view products')                
                print('2. add products')
                
                while True:
                    choice = int(input('enter your choice: '))
                    
                    if choice == 1:
                        for product in products:
                            print(f"name: {product['name']}, description: {product['description']}, price: {product['price']}")
                            
                    elif choice == 2: 
                        name = input('enter product name: ')
                        description = input('enter product description: ')
                        price = int(input('enter product price: '))
                        
                        new_product = {'name': name,
                                    'description': description,
                                    'price': price}
                        
                        products.append(new_product)
                        print('new product added successfully')
                        
                    else:
                        print('please choose 1 or 2')
                    
            break
        
    if not found: 
        print('invalid username or password')