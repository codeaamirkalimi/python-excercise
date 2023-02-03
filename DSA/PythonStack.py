class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Popped Element: ", self.stack[self.top])
            self.top = self.top - 1

    def printStack(self):
        temp = self.top
        if temp == -1:
            print("Stack Empty")
        else:
            while temp != -1:
                print(self.stack[temp])
                temp = temp - 1


if __name__ == '__main__':
    stack = Stack(5)
    stack.printStack()
    print("\n****************\n")
    stack.push(10)
    stack.printStack()
    print("\n****************\n")
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.printStack()
    print("\n****************\n")
    stack.pop()
    stack.printStack()
    print("\n****************\n")
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.printStack()
