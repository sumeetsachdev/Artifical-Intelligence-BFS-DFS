import numpy as np
import BFSDFS_goal as bd

"""Initializing 2-D matrix"""
grid = [["_"]*8 for _ in range(8)]

"""Converting into numpy array of type object to support all data-types (0,"#","*")"""
grid = np.array(grid,dtype=object)

"""Assigning the each cell of grid some value.
     Each empty cell is named using its index in grid/matrix"""
for i in range(8):
    for j in range(8):
        if i==0 or i==len(grid)-1 or j==0 or j==len(grid)-1:
            grid[i][j] = "#"
        else:
            grid[i][j] = (i,j)


"""Setting obstacles or walls in matrix"""
grid[2][2],grid[2][3],grid[2][4],grid[3][2],grid[3][4],grid[4][4],grid[5][2],grid[5][3],grid[5][4] = "#","#","#","#","#","#","#","#","#"

graph = {}


"""Converting the grid to adjacency-list graph.
      Each cell has those cells has its edges in which the player can travel.
      That, is if there is wall adjacent to cell, it is discarded as an edge"""
for i in range(1,7):
    for j in range(1,7):
        graph[(i,j)] = list()
        if grid[i][j] == "#":
            pass
        else:
            adjacent = [grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]]
            for k in adjacent:
                if k != "#":
                    graph[(i,j)].append(k)


"""Traversing from start state to goal state"""
path = bd.bfs_goal(graph,(6,1),(3,3))
print(path)


##def visualize_path(grid,pos_of_player,pos_of_food=(3,3)):
##    grid[tuple(pos_of_player)] = "P"
##    for z in grid:
##        for w in z:
##            print(w,end='\t')
##        print('\n')
##    print('\n\n\n\n\n')
##    return(grid)
##
##for node in path:
##    visualize_path(grid,node)
