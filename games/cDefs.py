#!/bin/python3
import os,sys
from pathlib import Path
root = Path(os.path.dirname( __file__ ))

import random
from typing import List, Tuple

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

class Grid:
    def __init__(self, width: int, height: int, shape: str):
        self.width = width
        self.height = height
        self.cells = [[None for _ in range(width)] for _ in range(height)]

        if shape == 'square':
            self.shape_func = self.square_shape_func
        elif shape == 'hexagon':
            self.shape_func = self.hexagon_shape_func
        else:
            raise ValueError(f'Unsupported shape: {shape}')

    def square_shape_func(self, x: int, y: int) -> List[Tuple[int, int]]:
        return [(x, y)]

    def hexagon_shape_func(self, x: int, y: int) -> List[Tuple[int, int]]:
        if y % 2 == 0:
            offsets = [(0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        else:
            offsets = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 0), (0, -1)]
        return [(x + ox, y + oy) for ox, oy in offsets if 0 <= x + ox < self.width and 0 <= y + oy < self.height]

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
        return self.shape_func(x, y)
class Shape:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        if name == 'square':
            self.width = size
            self.height = size
        elif name == 'hexagon':
            self.width = size * 2 - 1
            self.height = size * 2 - 1
        else:
            raise ValueError(f'Unsupported shape: {name}')

class Difficulty:
    def __init__(self, name: str, num_cells_to_fill: float):
        self.name = name
        self.num_cells_to_fill = num_cells_to_fill

diff_easy = Difficulty('easy', lambda shape: shape.width * shape.height * 0.3)
diff_medium = Difficulty('medium', lambda shape: shape.width * shape.height * 0.5)
diff_hard = Difficulty('hard', lambda shape: shape.width * shape.height * 0.7)

class Game:
    def __init__(self, shape: Shape, difficulty: Difficulty):
        self.shape = shape
        self.grid = Grid(shape.width, shape.height, shape.name)
        self.difficulty = difficulty


def num_cells_to_fill_easy(shape):
    return shape.width * shape.height // 5

def num_cells_to_fill_medium(shape):
    return shape.width * shape.height // 3

def num_cells_to_fill_hard(shape):
    return shape.width * shape.height // 2

def num_cells_to_fill_insane(shape):
    return shape.width * shape.height * 2 // 3

diff_easy = Difficulty('easy', num_cells_to_fill_easy)
diff_medium = Difficulty('medium', num_cells_to_fill_medium)
diff_hard = Difficulty('hard', num_cells_to_fill_hard)
diff_insane = Difficulty('insane', num_cells_to_fill_insane)

'''
cDefs = [
    Cell,
    Grid,
    Game,
    Shape,
    Difficulty,
    diff_easy,
    diff_medium,
    diff_hard,
    diff_insane,
]
'''
