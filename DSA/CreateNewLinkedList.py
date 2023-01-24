class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def addFirstNodeToLinkedList(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def addLastNodeToLinkedList(self, data):
        newNode = Node(data)
        if self.head == 'None':
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(0)
    second = Node(1)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printLinkedList()
    print("\n---------------------")
    llist.addFirstNodeToLinkedList(4)
    llist.printLinkedList()
    print("\n---------------------")
    llist.addFirstNodeToLinkedList(5)
    llist.printLinkedList()
    print("\n---------------------")
    llist.addLastNodeToLinkedList(6)
    llist.printLinkedList()
    print("\n---------------------")
    llist.addLastNodeToLinkedList(8)
    llist.printLinkedList()
