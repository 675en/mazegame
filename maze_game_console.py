# maze_game_console.py

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

def play():
    print("Добро пожаловать в лабиринт!")
    print("Управление: W (вверх), A (влево), S (вниз), D (вправо)\n")

    maze = generate_maze(ROWS, COLS)
    start = (1, 1)
    end = (ROWS - 2, COLS - 2)
    player_pos = list(start)
    move_count = 0

    while True:
        display_maze(maze, tuple(player_pos), start, end)

        if tuple(player_pos) == end:
            print(f"🎉 Вы прошли лабиринт за {move_count} ходов!")
            break

        move = input("Ход (W/A/S/D): ").upper()
        dy, dx = 0, 0
        if move == "W":
            dy = -1
        elif move == "S":
            dy = 1
        elif move == "A":
            dx = -1
        elif move == "D":
            dx = 1
        else:
            print("❌ Введите только W, A, S или D.")
            continue

        new_y = player_pos[0] + dy
        new_x = player_pos[1] + dx

        if maze[new_y][new_x] == ' ' or (new_y, new_x) == end:
            player_pos[0], player_pos[1] = new_y, new_x
            move_count += 1

if __name__ == "__main__":
    play()
