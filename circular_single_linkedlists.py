
class  Node:

    def __init__(self,value =None) -> None:
        self.value=value
        self.next= None

class CircularLinkedList: 

    def __init__(self) -> None:
        self.head = None
        self.tail= None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next


    def createCSLL(self, nodeValue):

        node = Node(nodeValue)
        node.next = node
        self.head =node
        self.tail =node
        return "The Circular Single Linked List Have been created"
    
    ####Insertion in Circular Linked Lists
    def insertCSLL(self,value,location):

        if self.head is None:
            return "The circular Single LnkedList Does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next =newNode
            elif location == 1:
                newNode.next =self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index <location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next=  newNode
                newNode.next = nextNode
            return "The node has been successfull "
        
    def traversalCSLL(self):
        if self.head is None:
            print("The list is empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode =tempNode.next
                if tempNode ==self.tail.next:
                    break
    ####Searchong a node in circular linked list
    def searchCSLL(self,nodeValue):
        if self.head is None:
            return "The list is empty"
        else:
            tempeNode = self.head
            while tempeNode:
                if tempeNode.value == nodeValue:
                    return tempeNode.value
                tempeNode =tempeNode.next
                if tempeNode == self.tail.next:
                    return "The node has not exist"









                 


        



    
circularSingleLinkedList=CircularLinkedList()
print(circularSingleLinkedList.createCSLL(1))
circularSingleLinkedList.insertCSLL(0,0)
circularSingleLinkedList.insertCSLL(2,1)
circularSingleLinkedList.insertCSLL(3,1)
circularSingleLinkedList.insertCSLL(2,2)

circularSingleLinkedList.traversalCSLL()
print(circularSingleLinkedList.searchCSLL(3))


print([node.value for node in circularSingleLinkedList])
         


