print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = name1.lower() + name2.lower()
true_total = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love_total = name.count("l") + name.count("o") + name.count("v") + name.count("e")
total = true_total* 10 + love_total

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")

elif total >= 40 and total<= 50:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"Your score is {total}.")