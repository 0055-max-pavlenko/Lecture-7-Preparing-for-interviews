class Stack():
    
    def __init__(self):
        self.stack = []
                       
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

symbols = {']':'[',')':'(','}':'{'}
my_stack = Stack()
sequence = input('Введите последовательность скобок:')

for item in sequence:
    
    if my_stack.size() == 0:
        my_stack.push(item)
    else:
        if item in symbols:
            if symbols[item] == my_stack.peek():
                my_stack.pop()
            else:
                my_stack.push(item)
        else:
            my_stack.push(item)

if my_stack.is_empty():
    print('Сбалансированно')
else:
    print('Несбалансированно')
