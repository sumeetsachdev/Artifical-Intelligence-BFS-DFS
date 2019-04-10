g = {'A':['B','D','G'],
        'B':['A','E','F'],
         'C':['F','H'],
         'D':['A','F'],
         'E':['B','G'],
         'F':['B','C','D'],
         'G':['A','E'],
         'H':['C']
    }


def dfs_goal(g,start,goal):
    if start not in g:
        print("Start state not in graph")
        return False
    visited = []
    stack = [[start]]
    if start == goal:
        return "Start and Goal states are same"
    while stack:
        path = stack.pop()
        curr = path[-1]
        if curr not in visited:
            for value in g[curr]:
                new_path = list(path)
                new_path.append(value)
                stack.append(new_path)
                if value == goal:
                    return new_path
            visited.append(curr)
            
def bfs_goal(g,start,goal):
    if start not in g:
        print("Start state not in graph")
        return False
    visited = []
    queue = [[start]]
    if start == goal:
        return "Start and Goal states are same"
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr not in visited:
            for value in g[curr]:
                new_path = list(path)
                new_path.append(value)
                queue.append(new_path)
                if value == goal:
                    return new_path
            visited.append(curr)
        
dfspath = dfs_goal(g,'A','F')
##print("DFS: ", path)
bfspath = bfs_goal(g,'A','F')
##print("BFS: ", path)
