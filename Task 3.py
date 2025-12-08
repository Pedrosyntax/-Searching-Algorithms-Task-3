from collections import deque

# BFS Implementation
def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if neighbor in maze and neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None

# DFS Implementation
def dfs(maze, start, goal):
    stack = [start]
    visited = set([start])
    parent = {start: None}
    while stack:
        current = stack.pop()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if neighbor in maze and neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    return None


## 3.2 - MAZE ##
maze = {
    (0,0),(0,1),(0,2),
    (1,0),(1,2),
    (2,0),(2,1),(2,2)
}

start = (0,0)
goal = (2,2)

bfs_path = bfs(maze, start, goal)
dfs_path = dfs(maze, start, goal)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)

## 3.3 MAZE ##
import time

def measure_time(algorithm, maze, start, goal):
    start_time = time.time()
    path = algorithm(maze, start, goal)
    end_time = time.time()
    return path, end_time - start_time

# BFS and DFS on small, medium, large mazes
small_maze = maze
medium_maze = {(x,y) for x in range(10) for y in range(10)}
large_maze = {(x,y) for x in range(50) for y in range(50)}

for name, m in [("Small", small_maze), ("Medium", medium_maze), ("Large", large_maze)]:
    bfs_path, bfs_time = measure_time(bfs, m, (0,0), (max(x for x,y in m), max(y for x,y in m)))
    dfs_path, dfs_time = measure_time(dfs, m, (0,0), (max(x for x,y in m), max(y for x,y in m)))
    print(f"{name} Maze -> BFS Time: {bfs_time:.6f}s, DFS Time: {dfs_time:.6f}s")

