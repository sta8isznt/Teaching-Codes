with open("pi_million_digits.txt") as file:
    lines = file.readlines()

pi = ""
for line in lines:
    pi += line.strip()

print(pi[:52])
