my_dict = {'Eua': [15, 20],
         'Panos' : 17,
         'Anna': 50}

for i in my_dict:
    print(my_dict[i])

print(my_dict['Panos'])

for name, numbers in my_dict.items():
    print(f"Ο αγαπημένος αριθμός του/της {name} είναι {numbers}")