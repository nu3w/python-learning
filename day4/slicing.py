# slicing: get multiple data(subset) from sequential datatype

# variable[start index : end_index + 1: step]     # end_index is exclusive
# print World
a = "Hello, World!"
print(a[7 : 12 : 2])

# print the characters in even index
print(a[::2])

# print the characters in odd index
print(a[1::2])

# print the reverse of the string
print(a[::-1])

a = "Mindrisers"      #print Mind, risers, riser, Mindriser
print(a[0 : 4])
print(a[4 : 10])
print(a[4 : 9])
print(a[0 : 9])

my_list = ["using", 'index', 'number', 'string', 'single', 'data']   # print 'number', 'string'
print(my_list[2 : 4])

word = "proing"
#add "gramm" and print the programming
print(word[0:3]+'gramm'+word[3:6])

# create a list of hobbies
hobbies = ['singing', 'dancing', 'cooking', 'reading']
# print out sentance including single hobbies in the list
print('I like', hobbies[0])
print('I like', hobbies[1])
print('I like', hobbies[2])
print('I like', hobbies[3])

# create a list of your details
a = ["Stella","NY","24","0123456789",['singing', 'dancing', 'cooking', 'reading']]
# print out sentance using the details in the list
print('My name is', a[0])
print('I am from', a[1])
print('I am', a[2], 'years old')
print('My contact number is', a[3])
print('My hobbies are', a[4][0], a[4][1], a[4][2], 'and', a[4][3])


a = ["name","add","80","contact"]
# change the age of user and print the output in tuple
a[2] = 25
print(tuple(a))