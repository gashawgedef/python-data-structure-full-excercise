

from sys import maxsize
from tracemalloc import start

from numpy import delete


class Queue:
    def __init__(self,maxSize) -> None:
        self.items=maxSize*[None]
        self.maxSize =maxSize
        self.start = -1
        self.top = -1
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ''.join(values )
    
    def isFull(self):
        if self.top+1 ==self.start:
            return True
        elif self.start ==0 and self.top+1==self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    def enqueue(self,value):
        if self.isFull():
            return "The queue is fulll"
        else:
            if self.top+1==self.maxSize:
                self.top =0
            else:
                self.top+=1
                if self.start ==-1:
                    self.start=0
            self.items[self.top]=value
            return "The elemenet has been added at the end of queue"
    def dequeue(self):
        if self.isEmpty():
            return "The circular Queue is Empty"
        else:
            firstElement =self.items[self.start]
            start= self.start
            if self.start == self.top:
                self.start =-1
                self.top = -1

            elif self.start+1==self.maxSize:
                self.start =0
            else:
                self.start +=1
            self.items[start]=None
            return firstElement
    def peek(self):
        if self.isEmpty():
            return "The list is Empty"
        else:
            return self.items[self.start]
    def delete(self):
        self.items= self.maxSize*[None]
        self.start = -1
        self.top = -1
         

    
customeQueue = Queue(4)
customeQueue.enqueue(1)
customeQueue.enqueue(2)
customeQueue.enqueue(3)
customeQueue.enqueue(4)
print(customeQueue.isFull())
print(customeQueue)


