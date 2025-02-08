class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)

stack = Stack()
def reverse_word(word):
    for letter in word:
        stack.push(letter)
    reversed_word = ""
    while not stack.is_empty():
        reversed_word += stack.pop()
    return reversed_word


print(reverse_word("hello")) # olleh