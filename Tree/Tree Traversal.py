class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    

def preOrder(root):
    if(root != None):
        print(root.data, end= " ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data, end= " ")
        inOrder(root.right)

def postOrder(root):
    if(root != None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end= " ")

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

print("Preorder traversal:")
preOrder(root) # Output: 1 3 2 4 5 8
print()  # For better readability
print("Inorder traversal:")
inOrder(root)  # Output: 2 3 4 1 5 8
print()  # For better readability   
print("Postorder traversal:")
postOrder(root) # Output: 2 4 3 8 5 1