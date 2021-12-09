class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return f'{self.items}'




q = Queue()
print("Is Empty ? ",q.isEmpty())
q.enqueue(1)
q.enqueue('two')
print("Size is: ",q.size())
print(q.dequeue())
print("Is Empty ? ",q.isEmpty())