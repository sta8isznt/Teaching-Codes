from random import randint
count = 0
players_choice = []

for i in range(6):
    num = int(input("Enter number between 1 and 49 (inclusive): "))
    players_choice.append(num)

lotto_numbers = []
for i in range(6):
    lotto_numbers.append(randint(1, 49))

for num in players_choice:
    if num in lotto_numbers:
        count += 1

print(f"You have successfully predicted {count} numbers")