
# Tree

## Today’s Learning (Day 11)

- Deletion in BST
	- Case 1: Node is a leaf (no children) → remove it
	- Case 2: Node has one child → replace node with its child
	- Case 3: Node has two children → replace node’s value with inorder successor (smallest in right subtree), then delete that successor node
	- Time complexity: $O(h)$ where $h$ is tree height (average $O(\log n)$ if balanced, worst $O(n)$ if skewed)

Code (insert/search/delete + inorder): [BST.py](BST.py)

## Today’s Learning (Day 10)

- What is a BST (Binary Search Tree)
	- A binary tree where for every node: left subtree values are smaller and right subtree values are larger
	- This property lets us search/insert by comparing and moving left/right
- Insertion in BST
	- Compare with current node
	- Go left if value is smaller, right if larger
	- Insert at the first empty spot (leaf position)
	- Note: in this implementation, duplicates are ignored (if value already exists, it returns the same node)
- Searching in BST
	- Same left/right decision as insertion until you find the value or hit `None`
	- Time complexity: $O(h)$ where $h$ is tree height (average $O(\log n)$ if balanced, worst $O(n)$ if skewed)

Code: [BST.py](BST.py)

Run:

```bash
python "Tree/BST.py"
```

## Today’s Learning (Day 9)

- Tree traversals (depth-first): preorder, inorder, postorder
- How traversal order changes what you "see" first (root/left/right)
- Reading traversal output for a given tree structure

## Previously (Day 8)

- Introduction to Trees (hierarchical, non-linear structure)
- Important terminology: root, parent/child, siblings, leaf, depth, height
- Types of trees: general (N-ary), binary tree, BST, full/complete/perfect, skewed
- Representations: linked nodes, array (for complete/perfect), parent array, adjacency list

## Notes

- Main notes: [Tree.md](Tree.md)

## Code

- Traversals (recursive DFS): [Tree Traversal.py](Tree%20Traversal.py)
- BST (insertion, search, inorder traversal): [BST.py](BST.py)

This script:

- Defines a basic `Node` (binary tree) structure
- Implements recursive traversals: `preOrder`, `inOrder`, `postOrder`
- Builds a small sample tree and prints each traversal order

Run:

```bash
python "Tree/Tree Traversal.py"
```

## Next

- Add level-order traversal (BFS) using a queue
- Add iterative DFS traversals (stack-based)
- Extend BST examples with iterative insert/search

