import random
x = ["rock", "paper", "scissors"]
pc = random.choice(x)
print(pc)
user = input("Enter rock paper or scissors: ")

if pc == user:
    print("Draw")
elif pc == "rock" and user == "scissors":
    print("pc wins")
elif pc == "rock" and user == "paper":
    print("user wins")
elif pc == "paper" and user == "rock":
    print("pc wins")
else:
    print("invalid input")