class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        if not self.is_empty():
            return  self.stack.pop()
        return -1
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
