from ast import Not
from platform import node


class Node:
    def __init__(self, value = None ) -> None:
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLinkedList(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head =newNode
            elif location == 1:
                newNode.next = None
                self.tail.next =newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index <location -1:
                     tempNode=tempNode.next
                     index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next= nextNode
                if tempNode == self.tail:
                    self.tail=newNode
    def traverseSLinkedList(self):
        if self.head is None:
            print("Single Linked list is empty")
        else:
            node = self. head
            while node is not None: 
                print(node.value)
                node = node.next
    def searchSLList(self, value):
        if self.head is None:
            print("The linked list is empty")
        else:
            node =self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return "The value does not exist"
        
    def deleteSLList(self,location):
        if self.head is None:
            print("The linked list value does not Exist")
        else:
            if location ==0:
                if self.head ==   self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head =self.head.next
            elif location == 1:
                 if self.head ==   self.tail:
                    self.head = None
                    self.tail = None
                 else:
                     node = self.head
                     index =0
                     while node is not None:
                         if node.next == self.tail:
                             break
                         node =node.next
                     node.next =None
                     self.tail =node
            else:
                tempNode =  self.head
                index = 0
                while index <location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next =nextNode.next

                



        
                      

                         
                  
                  
                     

                  











        


single_linked_list = SLinkedList()
single_linked_list.insertSLinkedList(1,0)
single_linked_list.insertSLinkedList(2,1)
single_linked_list.insertSLinkedList(3,1)
single_linked_list.insertSLinkedList(4,1)
single_linked_list.insertSLinkedList(5,1)
single_linked_list.insertSLinkedList(6,0)
single_linked_list.insertSLinkedList(5,3)



print([node.value for node in single_linked_list])
single_linked_list.traverseSLinkedList()
single_linked_list.deleteSLList(0)
print(single_linked_list.searchSLList(8))
single_linked_list.traverseSLinkedList()


 