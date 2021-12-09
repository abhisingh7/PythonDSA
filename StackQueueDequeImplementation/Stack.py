class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'{self.items}'

s = Stack()
print("Is Empty ? ",s.isEmpty())
s.push(1)
s.push('two')
print("Size is: ",s.size())
print(s.pop())
print(s.peek())
print("Is Empty ? ",s.isEmpty())
