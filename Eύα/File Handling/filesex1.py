with open("pi_digits.txt") as f:
    lines = f.readlines()
pi = ""
for line in lines:
    pi = pi + line.strip()
print(len(pi))