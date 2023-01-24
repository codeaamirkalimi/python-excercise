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

    def search(self, key):
        checkNode = self.head
        while checkNode is not None:
            if checkNode.data == key:
                return True
            else:
                checkNode = checkNode.next
        return False

    def deleteNode(self, key):
        checkNode = self.head
        if checkNode.data == key:
            self.head = self.head.next
        else:
            while checkNode.next is not None:
                if checkNode.next.data == key:
                    checkNode.next = checkNode.next.next
                    break
                else:
                    checkNode = checkNode.next


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
    print("\n---------------------")
    print(llist.search(54))
    llist.printLinkedList()
    print("\n---------------------")
    llist.deleteNode(5)
    llist.printLinkedList()
    print("\n---------------------")
    llist.deleteNode(0)
    llist.printLinkedList()
    print("\n---------------------")
    llist.deleteNode(8)
    llist.printLinkedList()
    print("\n---------------------")
    llist.deleteNode(1)
    llist.printLinkedList()
    print("\n---------------------")
    llist.deleteNode(3)
    llist.printLinkedList()
    print("\n---------------------")
    llist.deleteNode(33)
    llist.printLinkedList()
