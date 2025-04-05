sentence = input("Enter a sentence: ")

char_count = {}

for char in sentence.lower():
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)