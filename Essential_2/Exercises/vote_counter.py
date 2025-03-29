votes = ["Άννα", "Γιώργος", "Άννα", "Άννα", "Γιώργος", "Γιώργος", "Γιώργος", "Άννα", "Άννα", "Δημήτρης", "Δημήτρης", "Δημήτρης", "Δημήτρης", "Δημήτρης", "Μαριλένα", "Δημήτρης"]

results = {}

for i in range(len(votes)):
    results[votes[i]] = results.get(votes[i], 0) + 1

print("Total results: ")
for name, num_votes in results.items():
    print(name, num_votes)

max_name = "Άννα"
max_num_votes = results["Άννα"]
for name, num_votes in results.items():
    if num_votes > max_num_votes:
        max_num_votes = num_votes
        max_name = name

print(f"The winner is {max_name} with {max_num_votes} votes")

# my_list = [20, 4, 132, 40]
# max_element = my_list[0]
# for num in my_list:
#     if num > max_element:
#         max_element = num
# print(max_element)
