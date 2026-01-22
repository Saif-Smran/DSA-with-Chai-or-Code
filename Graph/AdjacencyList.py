class Graph:
    def __init__(self):
        self.adjList = {}
    
    def addVertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
    
    def addEdge(self, src, dest):
        self.addVertex(src)
        self.addVertex(dest)

        self.adjList[src].append(dest)
        self.adjList[dest].append(src)  # For undirected graph

    def printGraph(self):
        for vertex in self.adjList:
            # print(f"{vertex} -> {' '.join(map(str, self.adjList[vertex]))}")
            print(vertex, " ->", self.adjList[vertex])

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(3,4)
    g.addEdge(2,4)
    g.addEdge(1, 4)
    g.addEdge(3,5)
    g.addEdge(5,4)


    g.printGraph()