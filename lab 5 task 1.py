#task 1
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
    def pop(self, item):
        if stack.is_empty():
            return False
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
stack = Stack(4)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop(3))
print(stack.peek())
print(stack.is_empty())
print(stack.size())    

