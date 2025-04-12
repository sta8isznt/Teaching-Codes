pi = ""
with open("pi_million_digits.txt") as f:
    lines = f.readlines()

for line in lines:
    pi = pi + line.strip()
    
counter = 0
pi_first = ""
while counter < 52:
    pi_first += pi[counter]
    counter += 1

print(len(pi_first))
print(pi_first)