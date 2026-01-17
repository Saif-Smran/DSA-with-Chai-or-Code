class Graph: 
    def __init__(self, vertex):
        self.mat =[ [0] * vertex for x in range(vertex)]
        self.size = vertex
    
    def addEdgeUn(self, src, dest):
        if (0<= src < self.size and 0<= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge!")

    def addEdgeDir(self, src, dest):
        if (0<= src < self.size and 0<= dest < self.size):
            self.mat[src][dest] = 1
        else:
            print("Invalid Edge!")

    def addEdgeWei(self, src, dest, weight):
        if (0<= src < self.size and 0<= dest < self.size):
            self.mat[src][dest] = weight
        else:
            print("Invalid Edge!")
    
    def printGraph(self):
        for row in self.mat:
            print(" ".join(map(str, row)))

UnG = Graph(5)

UnG.addEdgeUn(0, 1)
UnG.addEdgeUn(0, 2)
UnG.addEdgeUn(1, 3)
UnG.addEdgeUn(2, 4)
UnG.addEdgeUn(2, 3)
UnG.addEdgeUn(3, 4)

print("Undirected Graph Adjacency Matrix:")
UnG.printGraph()