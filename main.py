import random

ROWS, COLS = 15, 15

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]