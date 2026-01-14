
# Tree

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
- Extend examples toward BST operations (insert/search/delete)

