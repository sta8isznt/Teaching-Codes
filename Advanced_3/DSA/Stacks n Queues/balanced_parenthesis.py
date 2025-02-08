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

def is_balanced(s):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

print(is_balanced("(())"))  # Output: True
print(is_balanced("([)]"))  # Output: False
