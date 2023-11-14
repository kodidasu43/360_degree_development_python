#password generator
import random

user_pwd_letters=int(input("How many letters would you like in your password?"))
user_pwd_symbols = int(input("How many symbols would you like?"))
user_pwd_numbers = int(input("How many numbers would you like?"))

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+','@']

#logic here
# password=""

# for character in range(1,user_pwd_letters+1):
    # password+=random.choice(letters_list)

# for symbol in range (1,user_pwd_symbols+1):
    # password+=random.choice(symbols_list)
    
# for symbol in range (1,user_pwd_numbers+1):
    # password+=random.choice(numbers_list)
    
# print(password)

password_list=[]

for character in range(1,user_pwd_letters+1):
    password_list+=random.choice(letters_list) #simsilar to .append method in list

for symbol in range (1,user_pwd_symbols+1):
    password_list+=random.choice(symbols_list)
    
for symbol in range (1,user_pwd_numbers+1):
    password_list+=random.choice(numbers_list)
    
print(password_list)

random.shuffle(password_list)

print(password_list)
password=""

for char in password_list:
    password+=char
    
print(f"your Password is {password}")









