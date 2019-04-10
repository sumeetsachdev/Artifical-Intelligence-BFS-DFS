from collections import defaultdict
from collections import deque as d
import BFSDFS_goal as bd


"""Create a board of current state to visualize better"""
def create_board(state):
    board,count = [],0
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(state[count])
            count = count + 1
        board.append(temp)
    return board

def print_board(board,state):
    board = create_board(state)
    for i in board:
        print(i)
    print('\n\n')


"""New state after 0 moves in any of 4 directions below"""
def left(state):
    pos = state.index("0")
    state = list(state)
    if pos in [0,3,6]:
        return None
    else:
        state[pos],state[pos-1] = state[pos-1],state[pos]
        state = "".join(state)
    return state

def right(state):
    pos = state.index("0")
    state = list(state)
    if pos in [2,5,8]:
        return None
    else:
        state[pos],state[pos+1] = state[pos+1],state[pos]
        state = "".join(state)
    return state

def up(state):
    pos = state.index("0")
    state = list(state)
    if pos in [0,1,2]:
        return None
    else:
        state[pos],state[pos-3] = state[pos-3],state[pos]
        state = "".join(state)
    return state

def down(state):
    pos = state.index("0")
    state = list(state)
    if pos in [6,7,8]:
        return None
    else:
       state[pos],state[pos+3] = state[pos+3],state[pos]
       state = "".join(state)
    return state


"""Each state is added as a node in the graph.
      States obtained after moving 0 in all possible directions are added as edges to the node"""
def graph(state,goal):
    graph = defaultdict(list)
    visited_queue = d()
    visited_queue.append(state)
    while visited_queue:
        state = visited_queue.popleft()
        if left(state) is not None and left(state) not in graph[state]:
            graph[state].append(left(state))
        if right(state) is not None and right(state) not in graph[state]:
            graph[state].append(right(state))
        if up(state) is not None and up(state) not in graph[state]:
            graph[state].append(up(state))
        if down(state) is not None and down(state) not in graph[state]:
            graph[state].append(down(state))
        for curr_state in graph[state]:
            if curr_state not in visited_queue:
                    visited_queue.append(curr_state)
                    if curr_state == goal:
                        return graph
    return graph

state = "052183476"
goal = "123456780"
board = create_board(state)
g = graph(state,goal) 
path = bd.bfs_goal(g,state,goal)
print(path)
for current_state in path:
    print_board(board,current_state)
