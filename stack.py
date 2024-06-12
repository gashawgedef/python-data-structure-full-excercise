

class Stack:
    def  __init__(self) -> None:
        self.list=[]
    def __str__(self) -> str:
         values=self.list.reverse()
         values=[str(x) for x in self.list]
         return '\n'.join(values)
    def isEmpty(self):
        return len(self.list)==0
    def push(self,item):
        self.list.append(item )
        return "The element has been successfully inserted"
    def pop(self):
        if self.isEmpty():
            return "There is no element in the list"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "There is no element in the list"
        else:
            return self.list[-1]
          

    
customStack =Stack()
print(customStack.isEmpty())
print(customStack.push(12))
print(customStack.push(13))
print(customStack.pop())
print(customStack.peek())