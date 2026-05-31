'''Practice 3: Sum of Leaf Nodes
Task: Calculate the sum of only the leaf nodes (nodes with no children) in a BST.
Input: A BST structure.
Goal: Sum of all nodes at the bottom of the tree.
Logic (Give If Needed):
Base Case: If root is None, return 0.
Leaf Check: If root.left is None AND root.right is None, return root.data.
Recursive Step: Return sum_leaves(root.left) + sum_leaves(root.right).'''


class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insert(root,key):
    if root is None:
        return Tree(key)
        
    if key<root.data:
        root.left=insert(root.left,key)
        
    else:
        root.right=insert(root.right,key)

    return root

def sum(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return root.data
        
    return sum(root.left)+sum(root.right)
    
root=Tree(10)
keys=[5,15,3,7,12,18]
for key in keys:
    root=insert(root,key)

print(sum(root))





        
