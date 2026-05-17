class Tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def largest_int(root):
        if root==None:
            return -1000
        
        left_max=Tree.largest_int(root.left)
        right_max=Tree.largest_int(root.right)
        return max(root.value, left_max, right_max)
        
        

root=Tree(10)
root.left=Tree(25)
root.right=Tree(15)
root.left.left=Tree(20)
root.left.right=Tree(30)
root.right.left=Tree(3)
root.right.right=Tree(5)

largest_val=Tree.largest_int(root)

print(f"The Largest int in this tree is: {largest_val}")
