pi = ""
with open("pi_digits.txt") as f:
    lines = f.readlines()

for line in lines:
    print(pi)
    pi = pi + line.strip()


print(pi)
print(len(pi))