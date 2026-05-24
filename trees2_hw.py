class Tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def smallest_int(root):
        if root==None:
            return 99999999
        
        left_min=Tree.smallest_int(root.left)
        right_min=Tree.smallest_int(root.right)
        return min(root.value, left_min, right_min)
        
        

root=Tree(10)
root.left=Tree(25)
root.right=Tree(15)
root.left.left=Tree(20)
root.left.right=Tree(30)
root.right.left=Tree(3)
root.right.right=Tree(5)

smallest_val=Tree.smallest_int(root)

print(f"The Smallest int in this tree is: {smallest_val}")
