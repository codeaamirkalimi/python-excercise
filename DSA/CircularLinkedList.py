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

    # adding node at the beginning of Circular Linked List
    # inserting node at the end of the Circular Linked List
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
