
# Graph

Learning Day 12: **Graph and Its Matrix Representation**
Learning Day 13: **Graph Adjacency List Representation**
Learning Day 14: **Graph Traversal — Depth First Search (DFS)**
Learning Day 15: **Graph Traversal — Breadth First Search (BFS)**

## What I Have learned

- Graph basics (vertices/nodes and edges)
- Types of graphs: undirected, directed, weighted
- Graph representation using **Adjacency Matrix**
- Graph representation using **Adjacency List**
- Graph traversal using **DFS** (iterative using a stack)
- Graph traversal using **BFS** (iterative using a queue)

## DFS (Depth First Search)

- DFS explores as deep as possible before backtracking.
- Common implementations: recursion (implicit stack) or iteration (explicit stack).
- Time complexity: $O(V^2)$ with an adjacency matrix (like in [DFS.py](DFS.py)); $O(V+E)$ with an adjacency list.

## BFS (Breadth First Search)

- BFS explores the graph **level by level** (all neighbors first, then their neighbors).
- Typical implementation uses a **queue**.
- In [BFS.py](BFS.py), BFS is implemented on an **adjacency matrix** and uses `collections.deque` for an efficient queue.
- Time complexity: $O(V^2)$ with an adjacency matrix (scans an entire row for each visited vertex); $O(V+E)$ with an adjacency list.
- Common use: shortest path in **unweighted** graphs (by number of edges), discovering levels, and connected-component traversal.

## Notes

- [Graph.md](Graph.md)

## Code

- [GraphAdjMatrix.py](GraphAdjMatrix.py) — basic adjacency-matrix graph class + example
- [AdjacencyList.py](AdjacencyList.py) — basic adjacency-list graph class + example
- [DFS.py](DFS.py) — DFS traversal using an explicit stack (adjacency matrix)
- [BFS.py](BFS.py) — BFS traversal using a queue (adjacency matrix)

## Run

```bash
python "Graph/GraphAdjMatrix.py"
```

```bash
python "Graph/AdjacencyList.py"
```

```bash
python "Graph/DFS.py"
```

```bash
python "Graph/BFS.py"
```
