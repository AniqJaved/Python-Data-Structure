from helpers import get_path, is_legal_pos, offsets, read_maze
from stack import Stack

#So we want to visit the nodes using dfs until we reach the goal node. For this we start with (0,0) node and there 
#i put that in the stack and also defined the predeceeors whihc will be used to trace the path from start to goal node.
#so we pop that node to check it it is goal node. Then if it is not we look for child nodes. For (0,0) child nodes are
#(0,1) and (1,0) and not the (1,1). So in this loop we are adding the child nodes in stack in clockwise order that is
#up,right,down,left. then we are checking that if the neighbour is on the legal position and also not a predecessor.
#By predeccor we mean a parent node, so if parent node was already in predecessor dict means we already had visited
#the that parent node and no need to do it again.
#prdecessor[neighbour] = current_value means that the parent of the neighboour is current value.

def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start:None}

    while not stack.is_empty():
        current_value = stack.pop()
        if current_value == goal:
            return get_path(predecessors,start,goal)
        for direction in ["up","right","down","left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_value[0] + row_offset,current_value[1] + col_offset)
            if is_legal_pos(maze,neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour] = current_value
    return None



    pass


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None