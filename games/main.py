import os
from pathlib import Path
from typing import List, Tuple
import random


class Cell:
    def __init__(self):
        self.value = None
        self.prefilled = False

    def set_value(self, value):
        if self.prefilled:
            raise ValueError('Cannot set the value of a prefilled cell')
        self.value = value

    def get_value(self):
        return self.value

    def set_prefilled(self, prefilled=True):
        self.prefilled = prefilled

    def is_prefilled(self):
        return self.prefilled

class NodeShape:
    def __init__(self, name: str, width: int, height: int, shape_func):
        self.name = name
        self.width = width
        self.height = height
        self.shape_func = shape_func

class Grid:
    def __init__(self, width: int, height: int, shape: NodeShape):
        self.width = width
        self.height = height
        self.cells = [[None for _ in range(width)] for _ in range(height)]
        self.shape = shape

    def get_cell(self, x: int, y: int) -> Cell:
        return self.cells[y][x]

    def set_cell(self, x: int, y: int, cell: Cell):
        self.cells[y][x] = cell

    def set_cell_value(self, x: int, y: int, value):
        self.get_cell(x, y).set_value(value)

    def get_cell_value(self, x: int, y: int):
        return self.get_cell(x, y).get_value()

    def set_cell_prefilled(self, x: int, y: int, prefilled=True):
        self.get_cell(x, y).set_prefilled(prefilled)

    def is_cell_prefilled(self, x: int, y: int) -> bool:
        return self.get_cell(x, y).is_prefilled()

    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        return self.shape.shape_func(x, y)

class Difficulty:
    def __init__(self, name: str, num_cells_to_fill):
        self.name = name
        self.num_cells_to_fill = num_cells_to_fill

class Game:
    def __init__(self, shape: NodeShape, difficulty: Difficulty):
        self.shape = shape
        self.grid = Grid(shape.width, shape.height, shape)
        self.difficulty = difficulty

class Node:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

class nodeShape:
    SQUARE = "square"
    CIRCLE = "circle"
    TRIANGLE = "triangle"

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for y in range(size)] for x in range(size)]

def generate_random_map(size, difficulty):
    grid = Grid(size)
    node_shapes = [nodeShape.SQUARE, nodeShape.CIRCLE, nodeShape.TRIANGLE]
    for i in range(size):
        for j in range(size):
            shape = random.choice(node_shapes)
            grid.grid[i][j] = Node(i, j, shape)
    return grid

def main():
    size = int(input("Enter the size of the grid (must be divisible by 3): "))
    while size % 3 != 0:
        size = int(input("Size must be divisible by 3, please enter a valid size: "))
    difficulty = int(input("Enter the difficulty level (1-10): "))
    while difficulty < 1 or difficulty > 10:
        difficulty = int(input("Difficulty level must be between 1-10, please enter a valid level: "))
    grid = generate_random_map(size, difficulty)
    filename = input("Enter a name for the HTML file to save the map: ")
    with open(f"{filename}.html", "w") as f:
        f.write("<html><head><title>Random Map</title></head><body>")
        for i in range(size):
            f.write("<div>")
            for j in range(size):
                node = grid.grid[i][j]
                if node.shape == nodeShape.SQUARE:
                    f.write("<div style='width:20px;height:20px;background-color:black;display:inline-block;margin-right:1px;margin-bottom:1px;'></div>")
                elif node.shape == nodeShape.CIRCLE:
                    f.write("<div style='width:20px;height:20px;border-radius:50%;background-color:black;display:inline-block;margin-right:1px;margin-bottom:1px;'></div>")
                elif node.shape == nodeShape.TRIANGLE:
                    f.write("<div style='width:0;height:0;border-left:10px solid transparent;border-right:10px solid transparent;border-bottom:20px solid black;display:inline-block;margin-right:1px;margin-bottom:1px;'></div>")
            f.write("</div>")
        f.write("</body></html>")

if __name__ == "__main__":
    main()
