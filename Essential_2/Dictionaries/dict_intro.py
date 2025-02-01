animals = {}
# print(type(animals))
animals[1] = 'dog' # pair-> 1:'dog'
animals[2] = 'cat'
animals[1] = 'turtle'
# print(animals)

my_list = ['dog', 'cat', 'turtle']
# print(my_list[1])
# print(animals.get(3, "This is not in my dict"))

# print(animals)
# if 3 in animals:
#     print('OK')

animals1 = animals.copy()
print(animals)
print(animals1)
animals1.pop(1)
print(animals)
print(animals1)