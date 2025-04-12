def reverse(word):
    i = len(word)-1
    while i >= 0:
        print(word[i], end='')
        i = i - 1

wrd = input("Enter a word to reverse: ")
reverse(wrd)