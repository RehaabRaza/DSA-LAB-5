from lab 5 task 1 import Stack
    
    def reverse_string(self, string):
        self.string = string.split()
        
        for i in self.string:
            stack.push(i)
        
        reversedString = ""
        while not stack.is_empty():
            reversedString += stack.pop(0)
        return reversedString
stack = Stack(5)
print(stack.reverse_string("hello"))