class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:
    def insert(self, rootNode, val):
        if rootNode is None:
            return Node(val)
        elif val > rootNode.data:
            rootNode.right = self.insert(rootNode.right, val)
        else:
            rootNode.left = self.insert(rootNode.left, val)
        return rootNode
