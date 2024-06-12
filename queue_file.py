from sqlalchemy import values


class  Queue:
    def __init__(self) -> None:
        self.items = []
    def __str__(self) -> str:
        values =[str(x) for x in self.items]
        return ' '.join(values)
    def isEmpty(self):
        if self.items ==[]:
            return True
        else:
            return False
    def enqueue(self,value):
        self.items.append(value)
        return "Element successfulyy inserted"
    def dequeue(self):
        if self.isEmpty():
            return "No Element found"
        else:
            return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            return "The list is empty"
        else:
            return self.items[0]
    def delete(self):
        self.items=None

custom =Queue()
custom.enqueue(10)
custom.enqueue(20)
custom.enqueue(30)
custom.enqueue(40)
print(custom.dequeue())
print(custom.peek())



print(custom)