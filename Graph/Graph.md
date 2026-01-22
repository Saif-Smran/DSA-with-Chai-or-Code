# Graph Basics

## 1. What is a Graph?

A **graph** is a data structure used to represent relationships between objects.

A graph is made of two main components:

- **Vertices (Nodes)**  
  These represent entities or points.

- **Edges**  
  These represent connections between vertices.

### Example Concept

If cities are vertices, then roads connecting them are edges.

### Example (Real-Life)

- **Google Maps**: cities = vertices, roads = edges
- **Social network**: people = vertices, friendships/follows = edges
- **Computer network**: devices = vertices, connections = edges

---

## 2. Basic Graph Terminology

| Term | Meaning |
|---|---|
| Vertex | A node in the graph |
| Edge | A connection between two vertices |
| Degree | Number of edges connected to a vertex |

---

## 3. Types of Graphs Learned

### 3.1 Undirected Graph

- Edges have no direction
- Connection works both ways

#### Example

```text
A --- B
|     |
C --- D
```

Here, A is connected to B and C, and the connection is mutual.

---

### 3.2 Directed Graph

- Edges have direction
- One-way connection

#### Example

```text
A --> B --> C
```

A can reach B, but B cannot reach A unless another edge exists.

---

### 3.3 Weighted Graph

- Each edge has a weight
- Weight can represent cost, distance, or time

#### Example

```text
A --5-- B
|       |
3       2
|       |
C --4-- D
```

---

## 4. Graph Representation

Graphs can be represented in two main ways:

1. Matrix Representation
2. List Representation

Today, both were practiced:

- **Adjacency Matrix** (2D matrix)
- **Adjacency List** (using a list / linked-list style per vertex)

---

## 5. Matrix Representation (Adjacency Matrix)

### 5.1 Definition

An **Adjacency Matrix** is a 2D matrix where:

- Rows represent vertices
- Columns represent vertices
- Cell value shows whether an edge exists

---

### 5.2 Example Graph

Vertices: A, B, C

Edges:
- A connected to B
- B connected to C

```text
A --- B --- C
```

---

### 5.3 Adjacency Matrix (Undirected Graph)

|   | A | B | C |
|---|---|---|---|
| A | 0 | 1 | 0 |
| B | 1 | 0 | 1 |
| C | 0 | 1 | 0 |

- `1` means edge exists
- `0` means no edge

---

### 5.4 Adjacency Matrix (Directed Graph)

If A → B and B → C

|   | A | B | C |
|---|---|---|---|
| A | 0 | 1 | 0 |
| B | 0 | 0 | 1 |
| C | 0 | 0 | 0 |

---

### 5.5 Adjacency Matrix (Weighted Graph)

|   | A | B | C |
|---|---|---|---|
| A | 0 | 5 | 0 |
| B | 5 | 0 | 3 |
| C | 0 | 3 | 0 |

Values represent weights instead of `1` or `0`.

---

## 6. Python Code for Adjacency Matrix

Repo example: see `Graph/GraphAdjMatrix.py`.

```python
# Number of vertices
n = 4

# Create adjacency matrix
graph = [[0 for _ in range(n)] for _ in range(n)]

# Add edges
graph[0][1] = 1
graph[1][0] = 1

graph[1][2] = 1
graph[2][1] = 1

# Print matrix
for row in graph:
    print(row)
```

---

## 7. List Representation (Adjacency List)

### 7.1 Definition

An **Adjacency List** stores, for each vertex, the list of its neighbors.

- Good for **sparse graphs** (few edges)
- Uses less memory than a matrix in many cases

In many languages this “list of neighbors” is implemented using a **Linked List**.
In Python, you’ll often use a normal `list`, but the idea is the same: each vertex points to a sequence of neighbors.

---

### 7.2 Undirected Graph (Adjacency List)

#### Example graph

```text
A --- B
|     |
C --- D
```

#### Adjacency list (concept)

```text
A: B -> C
B: A -> D
C: A -> D
D: B -> C
```

#### Basic Python code (undirected)

```python
class Graph:
    def __init__(self):
        self.adj = {}  # vertex -> list of neighbors

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        # undirected: add both directions
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def display(self):
        for v in self.adj:
            print(v, "->", self.adj[v])


g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.display()
```

---

### 7.3 Directed Graph (Adjacency List)

#### Example graph

```text
A --> B --> C
A --> D
```

#### Adjacency list (concept)

```text
A: B -> D
B: C
C:
D:
```

#### Basic Python code (directed)

```python
class DirectedGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        # directed: only u -> v
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)

    def display(self):
        for v in self.adj:
            print(v, "->", self.adj[v])


g = DirectedGraph()
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("A", "D")
g.display()
```

---

### 7.4 Weighted Graph (Adjacency List)

In a **weighted graph**, each edge has a number (weight): distance, cost, time, etc.

#### Example graph

```text
A --5-- B
|       |
3       2
|       |
C --4-- D
```

#### Adjacency list (concept)

```text
A: (B,5) -> (C,3)
B: (A,5) -> (D,2)
C: (A,3) -> (D,4)
D: (B,2) -> (C,4)
```

#### Basic Python code (weighted, undirected)

```python
class WeightedGraph:
    def __init__(self):
        self.adj = {}  # vertex -> list of (neighbor, weight)

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, w):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def display(self):
        for v in self.adj:
            print(v, "->", self.adj[v])


g = WeightedGraph()
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 3)
g.add_edge("B", "D", 2)
g.add_edge("C", "D", 4)
g.display()
```

---

### 7.5 Advantages of Adjacency List Representation

- Memory efficient for **sparse graphs** (stores only existing edges)
- Easy to iterate over neighbors (good for BFS/DFS)
- Adding an edge is usually fast (append to the neighbor list)
- Scales well when number of vertices is large but edges are limited

---

### 7.6 Disadvantages of Adjacency List Representation

- Checking whether an edge exists (u → v) can be slower (may require scanning the list)
- For **dense graphs**, it can be less convenient than a matrix
- Slightly more complex to implement for weighted/multi-graphs (needs tuples/objects)

---

## 8. Dijkstra ("Dizzy") Algorithm — Shortest Path

If “dizzy” means **Dijkstra**, here’s the basic idea:

- Works on **weighted graphs with non-negative weights**
- Finds the **shortest distance** from a start node to all other nodes
- Commonly implemented using a **min-heap (priority queue)**

### Basic Python code (Dijkstra with adjacency list)

```python
import heapq


def dijkstra(adj, start):
    """adj: dict[node] -> list[(neighbor, weight)]"""
    dist = {node: float("inf") for node in adj}
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)
    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist != dist[node]:
            continue

        for neighbor, weight in adj[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


graph = {
    "A": [("B", 5), ("C", 3)],
    "B": [("A", 5), ("D", 2)],
    "C": [("A", 3), ("D", 4)],
    "D": [("B", 2), ("C", 4)],
}

print(dijkstra(graph, "A"))
```

---

## 9. Advantages of Matrix Representation

- Simple and easy to implement
- Fast edge lookup using indices
- Good for dense graphs
- Clear visual structure

---

## 10. Disadvantages of Matrix Representation

- Uses more memory
- Inefficient for sparse graphs
- Adding or removing vertices is costly
- Many unused cells when edges are few

---

## 11. When to Use What?

- **Adjacency Matrix**: dense graphs, very fast edge checking, easy indexing
- **Adjacency List**: sparse graphs, faster neighbor iteration, memory efficient