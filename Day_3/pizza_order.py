print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

cheese = 0
peproni = 0
if size == "S":
    pizza = 15
    if add_pepperoni == "Y":
        peproni = 2
    
if size == "M" :
    pizza = 20
    if add_pepperoni == "Y":
        peproni = 3
    
if size == "L" :
    pizza = 25
    if add_pepperoni == "Y":
        peproni = 3
    
if extra_cheese == "Y":
    cheese = 1


print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${cheese + peproni + pizza}.")

