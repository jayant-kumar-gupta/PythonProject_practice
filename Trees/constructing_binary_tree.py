from Traverse_binary_tree import traverse

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def construction(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = construction(preorder[1:mid+1], inorder[:mid])
    root.right = construction(preorder[mid+1:], inorder[mid+1:])
    return root

node = construction([1,2,4,5,3,6], [4,2,5,1,3,6])
traverse(node)