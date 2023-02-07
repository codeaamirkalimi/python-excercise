class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AdjList:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size

    def addEdge(self, src, dest):
        newNode = Node(dest)
        if self.arr[src] is None:
            self.arr[src] = newNode
        else:
            last = self.arr[src]
            while last.next is not None:
                last = last.next
            last.next = newNode

    def addEdgeOnTop(self, src, dest):
        newNode = Node(dest)
        newNode.next = self.arr[src]
        self.arr[src] = newNode
