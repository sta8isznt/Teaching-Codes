ammount = int(input("Enter the ammount you have spent: "))
if ammount > 50 and ammount < 100:
    discount = 10/100 * ammount
    print("You should pay", ammount - discount, "€")
elif ammount > 100:
    discount = 20/100 * ammount
    print("You should pay", ammount - discount, "€")
else:
    print("No discount!")
