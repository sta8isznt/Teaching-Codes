from collections import deque

# BFS -> Ουρά
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
    
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

def bfs(root):
    if not root:
        return
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        node = q.dequeue()
        print(node.key, end=" ")
        for child in node.children:
            q.enqueue(child)

# DFS -> Στοίβα
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
  
def dfs(root):
    if not root:
        return
    s = Stack()
    s.push(root)
    while not s.is_empty():
        node = s.pop()
        print(node.key, end=" ")
        for child in node.children[::-1]:
            s.push(child)

# Παράδειγμα χρήσης
root = Node(1)
root.children.append(Node(2))
root.children.append(Node(3))
root.children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))
root.children[2].children.append(Node(7))

bfs(root)
print()
dfs(root)
