 

from platform import node


class Node:
    def __init__(self,value = None) -> None:

        self.value =value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node = node.next
    #insert node in linked list
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location ==0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next =None
                self.tail.next =newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index <location - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode  = tempNode.next
                tempNode =newNode
                newNode.next =nextNode


    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The List Doesn't exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
        return "The value doesn't exist in the list"
    
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None 





             





singleLinkedList = LinkedList()
singleLinkedList.insertSLL(1,1)
singleLinkedList.insertSLL(2,1)
singleLinkedList.insertSLL(3,1)
singleLinkedList.insertSLL(0,0)
singleLinkedList.insertSLL(0,3 )
print([node.value for node in singleLinkedList])
singleLinkedList.traverseSLL()
print(singleLinkedList.searchSLL(1))