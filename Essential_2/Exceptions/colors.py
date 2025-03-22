colors = ["red", "green", "blue"]

# print(colors[3])

try:
    print(colors[3])
except IndexError as something:
    print(something)

print("Hello")