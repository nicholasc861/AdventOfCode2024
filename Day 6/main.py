import os
from collections import deque

# Standard boilerplate to read input file
dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input')

# Read as string
f = open(input_file, "r").read()

if __name__ == "__main__":
    groups = f.split("\n")
    starting_pos = (0, 0)

    # Retrieve starting position of guard as (x, y) coordinate
    for idx, group in enumerate(groups):
        if ("^" in group):
            starting_pos = (idx, group.index("^"))
            
    dirs = deque([(-1, 0), (0, 1), (1, 0), (0, -1)])
    current_dir = dirs.popleft()
    num_visited = 1 # include starting position
    
    obstacle_encountered = {}
            
    queue = [(starting_pos[0] + current_dir[0], starting_pos[1] + current_dir[1])]
    while len(queue):
        (next_x, next_y) = queue.pop()
        
        if next_x < len(groups) and next_y < len(groups[0]) and next_x >= 0 and next_y >= 0:
            square = groups[next_x][next_y]
    
            if square != "#":
                # only count distinct squares
                if square == ".":
                    num_visited += 1
                    
                queue.append((next_x + current_dir[0], next_y + current_dir[1]))
                
                string = list(groups[next_x])
                string[next_y] = "X"
                groups[next_x] = ''.join(string)
            else:
                curr_x = next_x - current_dir[0]
                curr_y = next_y - current_dir[1]
                
                dirs.append(current_dir)
                current_dir = dirs.popleft()
                
                queue.append((curr_x + current_dir[0], curr_y + current_dir[1]))

    print(num_visited)