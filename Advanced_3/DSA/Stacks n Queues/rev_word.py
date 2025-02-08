from utils import Stack

# Reverse a given word using a stack

def reverse(word):
    stack = Stack()
    for char in word:
        stack.push(char)
    
    rev = ""
    while not stack.is_empty():
        char = stack.pop()
        rev += char
    return rev

print(reverse("hello"))