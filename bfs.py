from collections import defaultdict
class bfs:

    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        print(self.graph)


    def bfsImplementation(self,visited,v):
        visited.add(v)
        print(v, end=' ')

        for k in self.graph[v]:
            if k not in visited:
                self.bfsImplementation(visited,k)
                         
    def bfsStart(self,v):
        visited=set()
        self.bfsImplementation(visited,v)

b=bfs()
b.addEdge(0,1)
b.addEdge(1,2)
b.addEdge(1,3)
b.addEdge(1,4)
b.addEdge(2,5)
b.bfsStart(0)