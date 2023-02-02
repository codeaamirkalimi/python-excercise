class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, val):
        if self.top == self.size - 1:
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack[self.top] = val

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Popped Element", self.stack[self.top])
            self.top = self.top - 1
