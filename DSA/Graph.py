class AdjMatrix:
    def __init__(self, size):
        self.size = size
        self.arr = []
        for i in range(self.size):
            self.arr.append([0 for i in range(self.size)])
        print(self.arr)

    def addEdge(self, src, dest):
        self.arr[src][dest] = 1

    def printAdjMatrix(self):
        print("", end="\n")
        print("************************", end="\n")
        for i in range(self.size):
            print("", end="\n")
            for j in range(self.size):
                print(self.arr[i][j], end=" ")

    def removeEdge(self, src, dest):
        self.arr[src][dest] = 0


if __name__ == '__main__':
    adjMatrix = AdjMatrix(5)
    adjMatrix.addEdge(0, 1)
    adjMatrix.addEdge(0, 2)
    adjMatrix.printAdjMatrix()
    adjMatrix.removeEdge(0, 2)
    adjMatrix.printAdjMatrix()
