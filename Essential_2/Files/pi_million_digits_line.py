filename = 'pi_million_digits.txt'

with open(filename) as file:
    lines = file.readlines()

pi = ''
for line in lines:
    pi += line.strip()

print(f"{pi[:52]}")
print(len(pi))