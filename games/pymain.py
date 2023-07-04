#!/bin/python3
import random
from string import ascii_uppercase
from typing import List
from cDefs import *

def generate_map(shape: Shape, difficulty: Difficulty) -> str:
    # Initialize the game with the given shape and difficulty
    game = Game(shape, difficulty)

    # Fill in the specified number of cells with random values
    num_cells_to_fill = difficulty.num_cells_to_fill(shape)
    available_coords = [(x, y) for x in range(shape.width) for y in range(shape.height)]
    random.shuffle(available_coords)
    for i in range(num_cells_to_fill):
        x, y = available_coords.pop()
        game.grid.set_cell_value(x, y, random.randint(1, 9))

    # Generate the HTML code for the map
    html = '<html>\n<head>\n<style>\ntable {\nborder-collapse: collapse;\n}\n'
    html += 'td {\nborder: 1px solid black;\nwidth: 40px;\nheight: 40px;\ntext-align: center;\n}\n'
    html += 'td.prefilled {\nbackground-color: lightgray;\n}\n'
    html += '</style>\n</head>\n<body>\n<table>\n'
    for y in range(shape.height):
        html += '<tr>\n'
        for x in range(shape.width):
            value = game.grid.get_cell_value(x, y)
            if value is None:
                html += '<td></td>\n'
            else:
                classes = 'prefilled' if game.grid.is_cell_prefilled(x, y) else ''
                html += f'<td class="{classes}">{value}</td>\n'
        html += '</tr>\n'
    html += '</table>\n</body>\n</html>\n'

    # Save the HTML code to a file
    filename = f'map_{shape.name}_{difficulty.name}.html'
    with open(filename, 'w') as f:
        f.write(html)

    return filename
shape = Shape('hexagon', 4)
difficulty = diff_easy
filename = generate_map(shape, difficulty)
print(f'Map saved to {filename}')

