class Tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)

        if self.right:
            self.right.inorder_traversal()
        
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()


root=Tree(5)
root.left=Tree(4)
root.right=Tree(6)

root.left.left=Tree(3)
root.left.right=Tree(2)

print(f"Inorder Traversal: {root.inorder_traversal()}")

print(f"Preorder Traversal: {root.preorder_traversal()}")