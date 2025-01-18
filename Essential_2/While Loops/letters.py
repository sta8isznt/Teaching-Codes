message = input("Enter a message: ")

i=0
while i < len(message):
    if message[i] == 'l':
        i = i+1
        continue
    print(message[i])
    i = i + 1