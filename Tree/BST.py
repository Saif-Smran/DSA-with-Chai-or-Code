class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root
    if root.data > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    if root == None:
        print("Element not found")
        return
    if root.data == value:
        print("Element found:", root.data)
        return
    if root.data > value:
        search(root.left, value)
    else:
        search(root.right, value)


def get_Successor(root):
    root = root.right
    while root != None and root.left != None:
        root = root.left
    return root


def delete(root, value):
    if root == None:
        return None
    if root.data > value:
        root.left = delete(root.left, value)
    elif root.data < value:
        root.right = delete(root.right, value)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        else:
            succ = get_Successor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


# Example usage:
root = insert(None, 20)
root = insert(root, 30)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 18)
root = insert(root, 12)
print("Inorder traversal of the BST:")
inOrder(root)  # Output: 12 15 18 20 25 30 40 50

# print("\nSearching for elements:")
# search(root, 15)  # Output: Element found: 15
# search(root, 10)  # Output: Element not found

print("\nDeleting elements:")
root = delete(root, 20)
print("Inorder traversal after deleting 20:")
inOrder(root)  # Output: 12 15 18 25 30 40 50
