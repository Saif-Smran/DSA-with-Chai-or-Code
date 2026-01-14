class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, value):
    if (root == None):
        return Node(value)
    if (root.data == value):
        return root
    if (root.data > value):
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if (root == None):
        print("Element not found")
        return
    if (root.data == value):
        print("Element found:", root.data)
        return
    if (root.data > value):
        search(root.left, value)
    else:
        search(root.right, value)

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data, end= " ")
        inOrder(root.right)

# Example usage:
root = insert(None, 20)
root = insert(root, 30)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 23)
root = insert(root, 12)
print("Inorder traversal of the BST:")
inOrder(root)  # Output: 12 15 20 23 25 30 40 50

print("\nSearching for elements:")
search(root, 15)  # Output: Element found: 15
search(root, 10)  # Output: Element not found
