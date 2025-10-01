def is_balanced(expression):
    stack = []
    pairs = {'(': ')', '[' : ']', '{' : '}'}
    for i in expression:
        if i in '([{':
            stack.push(i)
            
        elif i in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()