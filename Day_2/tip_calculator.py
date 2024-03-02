print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

people = int(input("How many people to split the bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

per_person =  (bill + (bill * tip)/100)/people

per_person = format(per_person, ".1f")

print("Each person should pay: $", per_person,)