filename = 'pi_million_digits.txt'
with open(filename) as file:
    lines = file.readlines()

pi = ''
for line in lines:
    pi += line.strip()

bday = input("Enter your bday in the form of mmddyy: ")

if bday in pi:
    print("Your bday is in the first 1 million digits of pi!")
else:
    print("Your bday is not in the first 1 million digits of pi")