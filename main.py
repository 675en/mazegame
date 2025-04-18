import random

ROWS, COLS = 15, 15

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    def carve(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < rows - 1 and 0 < ny < cols - 1 and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                maze[x + dx][y + dy] = ' '
                carve(nx, ny)

    maze[1][1] = ' '
    carve(1, 1)
    maze[rows - 2][cols - 2] = ' '
    return maze

def display_maze(maze, player_pos, start, end):
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if (y, x) == player_pos:
                row += "P"
            elif (y, x) == start:
                row += "S"
            elif (y, x) == end:
                row += "E"
            else:
                row += maze[y][x]
        print(row)
    print()