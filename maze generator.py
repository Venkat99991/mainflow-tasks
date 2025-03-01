import random

def generate_maze(width, height):
    maze = [['1' for _ in range(width)] for _ in range(height)]
    stack = [(1, 1)]
    maze[1][1] = '0'

    def neighbors(x, y):
        dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        result = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == '1':
                result.append((nx, ny))
        return result

    while stack:
        cx, cy = stack[-1]
        nbs = neighbors(cx, cy)
        if nbs:
            nx, ny = random.choice(nbs)
            stack.append((nx, ny))
            maze[nx][ny] = '0'
            maze[(cx + nx) // 2][(cy + ny) // 2] = '0'
        else:
            stack.pop()

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) == end:
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == '0' and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx, ny))
    return False

width, height = 11, 11
maze = generate_maze(width, height)
print_maze(maze)
print(solve_maze(maze, (1, 1), (height-2, width-2)))  # Output: True or False based on the maze
