import random

print("Welcome to the Password Generator!")

letter = int(input("How many letters would you like in your password?\n"))

symbol = int(input("How many symbol would you like in your password?\n"))

num = int(input("How many number would you like in your password?\n"))

pass_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
pass_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pass_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

for i in range(0, letter):
    password.append(random.choice(pass_letter))
for i in range(0, num):
    password.append(random.choice(pass_numbers))
for i in range(0,symbol):
    password.append(random.choice(pass_symbols))

random.shuffle(password)

strs_pass = ""

for i in password:
    strs_pass += i

print(strs_pass)