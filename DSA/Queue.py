class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.last = 0
        self.first = 0

    def enqueue(self, value):
        if self.last == self.size:
            print("Queue is Full")
        else:
            self.queue[self.last] = value
            self.last = self.last + 1

    def dequeue(self):
        if self.first == self.last:
            print("Queue is empty")
        else:
            print("Dequeue Element: ", self.queue[self.first])
            self.first = self.first + 1

    def printQueue(self):
        temp = self.first
        if temp == self.last:
            print("Queue Empty")
        else:
            while temp != self.last:
                print(self.queue[temp])
                temp = temp + 1


if __name__ == '__main__':
    queue = Queue(5)
    queue.printQueue()
    print("\n****************\n")
    queue.enqueue(10)
    queue.printQueue()
    print("\n****************\n")
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.printQueue()
    print("\n****************\n")
    queue.enqueue(60)
    queue.printQueue()
    queue.dequeue()
    queue.printQueue()
    print("\n****************\n")
    queue.dequeue()
    queue.dequeue()
    queue.printQueue()
    print("\n****************\n")
    queue.printQueue()
