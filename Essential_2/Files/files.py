# Header -> Open the file
# Body -> Processes the contents of the file

with open("pi_digits.txt") as file:
    contents = file.read()

print(contents.rstrip())

with open("pi_digits.txt") as f:
    for line in f:
        print(line.strip(), end="")

print()
with open("pi_digits.txt") as f:
    lines = f.readlines()
print(lines)

print(len("Hello"))

str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

pi = ""
with open("pi_digits.txt") as f:
    lines = f.readlines()

for line in lines:
    print(pi)
    pi = pi + line.strip()


print(pi)