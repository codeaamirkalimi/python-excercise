class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printDoublyLinkedList(self):
        global last
        temp = self.head
        print("Forward Printing\n----------------\n")
        while temp is not None:
            print(temp.data, end=" ")
            if temp.next is None:
                last = temp
            temp = temp.next
        print("\nBackward Printing\n---------------\n")
        temp = last
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev

    def insertFirst(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        temp.prev = self.head

    def insertLast(self, data):
        global last
        temp = self.head
        if temp.next is None:
            self.head.data = data
        else:
            while temp.next is not None:
                temp = temp.next
            last = temp
            temp = Node(data)
            temp.prev = last
            last.next = temp


if __name__ == "__main__":
    doublyLinkedList = DoublyLinkedList()
    firstNode = Node(10)
    secondNode = Node(20)
    thirdNode = Node(30)
    fourthNode = Node(60)
    doublyLinkedList.head = firstNode
    firstNode.next = secondNode
    secondNode.prev = firstNode
    secondNode.next = thirdNode
    thirdNode.prev = secondNode
    thirdNode.next = fourthNode
    fourthNode.prev = thirdNode

    doublyLinkedList.printDoublyLinkedList()
    print("\n********************\n")
    doublyLinkedList.insertFirst(40)
    doublyLinkedList.printDoublyLinkedList()
    print("\n********************\n")
    doublyLinkedList.insertFirst(80)
    doublyLinkedList.printDoublyLinkedList()
    print("\n********************\n")
    doublyLinkedList.insertLast(1000)
    doublyLinkedList.printDoublyLinkedList()
    print("\n********************\n")
    doublyLinkedList.insertLast(500)
    doublyLinkedList.printDoublyLinkedList()
