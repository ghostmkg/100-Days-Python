import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

lis = [rock, paper, scissors]
if user < 2 and user > 0:
    print(lis[user])    

comp = random.randint(0,2)
print("Computer Choose:")
print(lis[comp])

if user > 2 or user < 0:
    print("You Typed an Invalid Number, You lose!")
elif comp == user:
    print("Match Tie")

elif (user == 0 and comp == 2 ) or (user == 2 and comp == 1 ) or (user == 1 and comp == 0 ):
    print("You Win")
else:
    print("You loss")


