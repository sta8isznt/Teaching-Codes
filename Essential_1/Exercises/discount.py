money = int(input("Enter the ammount you have spent: "))

if money > 100:
    E = (20 / 100) * money
    T = money - E
    print(T)
elif money > 50:
    y = (10/100) * money
    T = money - y
    print(T)
else: # Το else δεν παίρνει συνθήκη!
    print("NO discount!")