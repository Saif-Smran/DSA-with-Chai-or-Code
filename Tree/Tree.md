# Day 8: Introduction to Trees — Types & Representation

Trees are one of the most important DSA topics because they model **hierarchies** (file system, DOM, org chart) and also power fast searching (BST), indexing (heaps), and range queries.

---

## 1) What is a Tree?

A **tree** is a **non-linear** data structure made of nodes connected by edges.

### Key Properties (for a rooted tree)
- There is exactly one **root** node.
- Every node (except root) has exactly one **parent**.
- A node can have **0 or more children**.
- There are **no cycles**.
- There is exactly **one simple path** from the root to any node.

---

## 2) Tree Terminology

- **Root**: topmost node (level 0)
- **Parent** / **Child**: relation between connected nodes
- **Siblings**: nodes with the same parent
- **Leaf (External node)**: node with no children
- **Internal node**: node with at least one child
- **Edge**: connection between two nodes
- **Degree (of node)**: number of children
- **Depth (of node)**: number of edges from root to that node
- **Height (of node)**: number of edges on the longest path from that node to a leaf
- **Height (of tree)**: height of the root

Example (levels / depth):

```text
        A        (level 0)
      /   \
     B     C     (level 1)
    / \
   D   E          (level 2)
```

---

## 3) Common Types of Trees

### 3.1 General Tree (N-ary Tree)
A node can have **any number of children**.

### 3.2 Binary Tree
Each node has **at most 2 children**: `left` and `right`.

Valid binary tree:

```text
    A
   / \
  B   C
```

Invalid (more than 2 children):

```text
    A
  / | \
 B  C  D    (❌ not a binary tree)
```

### 3.3 Binary Search Tree (BST)
A binary tree with ordering rules:
- left subtree values < node value
- right subtree values > node value

Valid BST:

```text
      50
     /  \
   30    70
  / \   / \
 20 40 60 80
```

### 3.4 Full (Strict) Binary Tree
Every node has either **0 or 2 children**.

```text
    A
   / \
  B   C
```

### 3.5 Complete Binary Tree
- All levels are completely filled **except possibly the last**
- Last level is filled **from left to right**

```text
        A
      /   \
     B     C
    / \   /
   D   E F
```

### 3.6 Perfect Binary Tree
All internal nodes have 2 children **and** all leaves are at the same level.

```text
        A
      /   \
     B     C
    / \   / \
   D   E F   G
```

### 3.7 Skewed / Degenerate Tree
Every node has only one child (shape becomes like a linked list).

Left skew:

```text
  A
 /
B
/
C
```

Right skew:

```text
A
 \
  B
   \
    C
```

---

## 4.6 Degenerate Tree

A **degenerate tree** behaves like a **linked list** (each node has only one child).

- Height can become $n-1$ (for $n$ nodes)
- Many operations degrade to worst-case linear time (like a linked list)

---

## 4.7 Extended Binary Tree

An **extended binary tree** is made by adding **dummy (NULL) nodes** so that every internal node has exactly 2 children.

Why it’s mentioned:
- It helps explain how **array representation** can “fill gaps” in an incomplete tree.

Drawbacks:
- Wastes memory
- Number of dummy nodes can grow quickly with height

---

## 5. Binary Tree Representation

## 5.1 Array Representation

Works best when the tree is **complete or close to complete**.

### Index Formula (0-based)
- Left child index = $2i + 1$
- Right child index = $2i + 2$
- Parent index = $\lfloor (i - 1) / 2 \rfloor$

### Logical View

```text
    A
  /   \
 B     C
/ \
D   E
```

### Physical View (Array)

```text
Index: 0  1  2  3  4
Value: A  B  C  D  E
```

### Drawbacks
- Wastes memory for sparse trees (many empty slots)
- Not a natural fit for general / highly unbalanced trees

---

## 5.2 Linked (Node) Representation

Each node stores:
- `data`
- `left` pointer/reference
- `right` pointer/reference

### Structure

```text
| data | left | right |
```

### Example

```text
    A
  /   \
 B     C

A.left  -> B
A.right -> C
B.left  -> NULL
B.right -> NULL
```

### Advantages
- No memory waste for missing children
- Works for any tree shape

### Drawbacks
- No direct indexing like arrays
- Traversals usually require recursion or an explicit stack/queue

---

## 6. Comparison Summary

| Feature | Array | Linked Representation |
|---|---|---|
| Memory usage | High for sparse trees | Efficient |
| Access pattern | Direct indexing | Pointer-based |
| Flexibility | Low | High |
| Best for | Complete/perfect trees | Any tree shape |

---

## 7) What to Practice Next

1) Write the array indices for a complete tree of 7 nodes.
2) Draw a complete vs perfect tree (spot the difference).
3) Next topic to learn: **tree traversals**
- Preorder (Root-Left-Right)
- Inorder (Left-Root-Right)
- Postorder (Left-Right-Root)
- Level order (BFS)
