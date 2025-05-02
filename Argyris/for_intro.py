number = int(input("Enter a number: "))

for x in range(number):
    # x will take the values from 0 to number - 1
    if x % 2 == 0:
        print(x)