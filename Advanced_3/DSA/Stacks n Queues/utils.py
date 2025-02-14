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
    
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def is_empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
