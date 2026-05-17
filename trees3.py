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
            
    def insert(self,value):
        if value<self.value:
            if self.left is None:
                self.left=Tree(value)
            else:
                self.left.insert(value)
                
        else:
            if self.right is None:
                self.right=Tree(value)
            else:
                self.right.insert(value)
            
    def inorder_successor(self):
            current=self.right
            while current.left is not None:
                current=current.left
            return current
        

root=Tree(10)
root.left=Tree(15)
root.right=Tree(5)
root.left.left=Tree(20)
root.left.right=Tree(25)

root.inorder_traversal()
successor=root.inorder_successor().value
print(f"successor: {successor}")
            