import os
import json
import random
from modules.equation import Equation
from modules.puzzle import Puzzle

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), 'configs', 'config.json')
with open(config_path, 'r') as f:
    config = json.load(f)

# Create puzzle
puzzle = Puzzle(
    shape=config['shape'],
    num_equations=config['num_equations'],
    outline=config['outline'],
    difficulty=config['difficulty']
)

# Save puzzle as printable file
output_dir = os.path.join(os.path.dirname(__file__), 'data', 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, 'puzzle.txt')
with open(output_path, 'w') as f:
    f.write(puzzle.to_string())
