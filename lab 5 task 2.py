#part 2
class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            return False
        else:
            return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return False
        else:
            return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.front())
print(queue.is_empty())
print(queue.size())