from sqlalchemy import values


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    def __str__(self) -> str:
        return str(self.value)
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode =curNode.next

class Queue:
    def __init__(self) -> None:
        self.linkedList = LinkedList()
    def __str__(self) -> str:
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    def enqueue( self,value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    def isEmpty(self):
        if self.linkedList.head ==None:
           return True
        else:
            return  False
    def dequeue(self):
        if self.isEmpty():
            return "The List is Empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail =None
            else:
                self.linkedList.head =self.linkedList.head.next
        return tempNode
    
    def delete(self):
        self.linkedList.head =None
        self.linkedList.tail=None

    def peek(self):
        if self.isEmpty():
            return "The list is empty"
        else:
            return self.linkedList.head
        


    






customQueue =Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.peek())
         
      

    


