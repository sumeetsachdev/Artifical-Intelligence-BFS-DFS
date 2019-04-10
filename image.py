import cv2
import numpy as np
import BFSDFS as bd
from collections import defaultdict


"""Reading the image and normalizing it by max value of pixel i.e. 255"""
img = cv2.imread('binary.png',0)/255.0


graph = defaultdict(list)


"""Converting the image matrix to graph using adjacency list.
      Each node of graph is the tuple-index of the matrix"""
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        graph[(i,j)] = list()
        adjacent = [[i-1,j-1],[i,j-1],[i+1,j-1],[i-1,j],[i,j-1],[i+1,j],[i-1,j+1],[i,j+1],[i+1,j+1]]
        illegal_indices = [(-1,x) for x in range(img.shape[1])] + [(x,-1) for x in range(img.shape[0])]
        if img[i][j] == 1:
            for neighbor in adjacent:
                try:
                    if img[tuple(neighbor)] == 1 and tuple(neighbor) not in illegal_indices:
                        graph[(i,j)].append(tuple(neighbor))
                except IndexError:
                    pass

"""Finding the total number of non-empty nodes in the graph"""
n_nodes = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] == 1 and (i,j) not in n_nodes:
            n_nodes.append((i,j))



"""Finding the connected components using BFS"""
visited = []
connected_components = 0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] == 1 and (i,j) not in visited:
            path = bd.bfs(graph,(i,j))
            connected_components += 1
            visited.extend(path)

print("Total number of connected components in this graph are: ", connected_components)
