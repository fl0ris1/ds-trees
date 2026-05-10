class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder_traversal()

    def insert(self,data):
        if data<self.data:
            if self.left is None:
                self.left = Node(data)

            else:
                self.left.insert(data)

        else:

            if self.right is None:
                self.right = Node(data)

            else:
                self.right.insert(data)


root=Node(10)
root.insert(56)
root.insert(12)
root.insert(16)
root.insert(4)
root.insert(99)
root.insert(100)

root.inorder_traversal()