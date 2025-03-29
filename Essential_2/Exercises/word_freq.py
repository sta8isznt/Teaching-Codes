# Split a string into its words: split()
sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)):
    words[i] = words[i].lower()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, counter in word_count.items():
    print(f"{word} appears {counter} times in your sentence")
    # print(word, "appears", counter, "times in your sentence")
