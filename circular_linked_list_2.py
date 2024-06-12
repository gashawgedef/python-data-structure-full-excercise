

from operator import index


class Node:
    def __init__(self,value) -> None:
        self.value =value
        self.next =None

class LinkedList:
    def __init__(self) -> None:
        self.head =None
        self.tail =None

    def __iter__(self):
        node =self.head
        while node:
            yield node
            if node.next == self.head:
             break
            node =node.next
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail =  node
        return node.value


# Insertion in Circular Linked List
    def insertCSLL(self, location, value):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode  
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next =newNode
                self.tail = newNode
            else:
                tempNode =self.head
                index =0
                while index <location -1:
                    tempNode =tempNode.next
                    index += 1
                    nextNode = tempNode.next
                    tempNode.next =newNode
                    newNode.next =nextNode
            return "The node has been successfully inserted"
    ##Traversal of Single linked List
    def traversalCSLL(self):
         if self.head is None:
             return "Circular single list is empty"
         else:
             tempNode = self.head
             while tempNode:
                 print(tempNode.value)
                 tempNode =tempNode.next
                 if tempNode == self.tail.next:
                     break
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "The single linked list is empty"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
    ####Delete from linked list
    def deleteCSLL(self,location):
        if self.head is None:
            print("There is no node in thwe list")
        else:
            if location == 0:
                if self.head ==self.tail:
                    self.head =None
                    self.tail =None
                    self.tail.next =None
                else:
                    self.head =self.head.next
                    self.tail.next =self.head
            elif location ==1:
                if self.head ==self.tail:
                    self.head =None
                    self.tail =None
                    self.tail.next =None
                else:
                    tempNode =self.head
                    while tempNode:
                        if tempNode ==self.tail:
                            break 
                        tempNode =tempNode.next
                    tempNode.next =self.head
                    self.tail =tempNode
            else:
                node = self.head
                index =0
                while index <location-1:
                    node = node.next
                    index += 1
                nextNode=tempNode.next
                tempNode.next =nextNode.next
                 


                    




        




            
                
circularSLL= LinkedList()
print(circularSLL.createCSLL(9))
circularSLL.insertCSLL(0,10)
circularSLL.insertCSLL(1,11)
circularSLL.insertCSLL(2,12)
circularSLL.insertCSLL(3,13)
circularSLL.insertCSLL(4,14)
circularSLL.insertCSLL(5,15)
circularSLL.traversalCSLL()
print(circularSLL.searchCSLL(14))   

print([node.value for node in circularSLL])
circularSLL.deleteCSLL(0)
print([node.value for node in circularSLL])
             
             
 
        