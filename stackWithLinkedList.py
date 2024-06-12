
class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next =None
class LinkedList:
    def __init__(self) -> None:
        self.head= None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode=curNode.next
class Stack:
    def __init__(self) -> None:
        self.linkedList=LinkedList()
    def __str__(self) -> str:
        values = [str(node.value) for node in self.linkedList]
        return '\n'.join(values)
    def isEmpty(self):
        return self.linkedList.head==None
    def push(self,value):
        node =Node(value)
        node.next=self.linkedList.head
        self.linkedList.head=node
    def pop(self):
        if self.isEmpty():
            return "There is element in the list"
        else:
            nodeValue=self.linkedList.head
            self.linkedList.head=self.linkedList.head.next
            return nodeValue.value
    def peek(self):
        if self.linkedList.head ==None:
            return "There is no value in the stack"
        else:
            return self.linkedList.head.value

    def delte(self):
        self.linkedList.head = None



custumStack=Stack()
print(custumStack.isEmpty())
custumStack.push(12)
custumStack.push(13)
custumStack.push(14)
custumStack.push(15)
print(custumStack)
print(custumStack.pop())
# print(custumStack.isEmpty())
# print(custumStack.isEmpty())
custumStack.delte()
print(custumStack)
