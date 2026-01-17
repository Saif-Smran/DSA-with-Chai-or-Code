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

Today, only **Matrix Representation** was learned.

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

## 7. Advantages of Matrix Representation

- Simple and easy to implement
- Fast edge lookup using indices
- Good for dense graphs
- Clear visual structure

---

## 8. Disadvantages of Matrix Representation

- Uses more memory
- Inefficient for sparse graphs
- Adding or removing vertices is costly
- Many unused cells when edges are few