class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def printCircularLinkedList(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

    def addNodeAtStart(self, data):
        newNode = Node(data)
        temp = self.head
        if temp == None:
            newNode.next = newNode
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next

            newNode.next = self.head
            self.head = newNode
            lastNode.next = newNode

    # inserting node at the end of the Circular Linked List
    def insertAtEnd(self, data):
        newNode = Node(data)
        lastNode = self.head
        while lastNode.next != self.head:
            lastNode = lastNode.next

        lastNode.next = newNode
        newNode.next = self.head
    # search node in circular linked list
    # deleting node in circular linked list


if __name__ == '__main__':
    circularLinkedList = CircularLinkedList()
    circularLinkedList.head = Node(10)
    middle = Node(20)
    last = Node(30)
    circularLinkedList.head.next = middle
    middle.next = last
    last.next = circularLinkedList.head
    circularLinkedList.printCircularLinkedList()
    print("\n******************\n")
    circularLinkedList.addNodeAtStart(5)
    circularLinkedList.printCircularLinkedList()
    print("\n******************\n")
    circularLinkedList.insertAtEnd(35)
    circularLinkedList.printCircularLinkedList()
