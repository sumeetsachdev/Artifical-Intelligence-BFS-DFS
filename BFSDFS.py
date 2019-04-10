##class graph:
##    def __init__(self):
##        self.graph = {}
##    def add(self,name,vertices):
##        self.graph[name] = vertices
##        return self.graph
##    def dfs(self,start):
##        if start in self.graph and goal in self.graph:
##            visited = []
##            stack = [start]
##            while stack:
##                v = stack.pop()
##                if v not in visited:
##                    visited.append(v)
##                    stack.append(graph[v])
##            return visited
##        else:
##            print("Either initial state or goal state not in graph")
##            return False
##
##g = graph()

##nv = int(input("Enter the number of vertices: "))
##
##for i in range(1,nv+1):
##    v = input("Enter the name of the vertex: ")
##    e = []
##    ne = int(input("Enter the number of vertices: "))
##    for j in range(ne):
##        e.append(input("Enter the edge: "))
##    g.add(v,e)
##
##print(g.dfs('a'))
##print(g.graph)


g = {'A':['B','D','G'],
        'B':['A','E','F'],
         'C':['F','H'],
         'D':['A','F'],
         'E':['B','G'],
         'F':['B','C','D'],
         'G':['A','E'],
         'H':['C']
    }


def dfs(g,start):
    if start not in g:
        print("Start state not in graph")
        return False
    visited = []
    stack = [start]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            for value in g[curr]:
                if value not in visited:
                    stack.append(value)
    return visited

def bfs(g,start):
    if start not in g:
##        print("Start state not in graph")
        return None
    visited = []
    queue = [start]
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            visited.append(curr)
            for value in g[curr]:
                if value not in visited:
                    queue.append(value)
    return visited


d = dfs(g,'A')
b = bfs(g,'A')

##print('DFS Traversal: ', '->'.join(d))
##print('BFS Traversal: ', '->'.join(b))

        

