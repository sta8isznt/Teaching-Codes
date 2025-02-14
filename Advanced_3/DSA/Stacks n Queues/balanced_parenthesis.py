from utils import Stack

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

print(is_balanced("(())"))
print(is_balanced("([)]"))
