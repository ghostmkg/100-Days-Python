import random

names = input().split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

num = random.randint(0, len(names)-1)

print(f"{names[num]} is going to buy the meal today!")