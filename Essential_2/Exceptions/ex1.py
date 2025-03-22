try:
    print("Hello")
    print(10 / 0)
except ZeroDivisionError as e:
    print("I cannot do division with zero")
try:
    colors = ['red', 'green', 'blue']
    print(colors[3])
except IndexError as e:
    print(e)
