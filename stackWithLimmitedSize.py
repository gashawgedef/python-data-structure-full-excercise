

from sys import maxsize


class Stack:
    def __init__(self,maxsize) -> None:
        self.maxSize=maxsize
        self.list =[]

    def __str__(self) -> str:
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        return len(self.list)==0
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value )
            return "The lement has been successfully inserted"
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]
    def delete(self):
        self.list = None


customStack =Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack)
