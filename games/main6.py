from typing import List
from dominate import tags as tg
import random

from dominate import tags


from dominate import tags


class Node:
    def __init__(self, node_type):
        self.type = node_type
    
    def get_html(self):
        if self.type == 'number':
            return tags.div('', cls='node number')
        elif self.type == 'operator':
            return tags.div('', cls='node operator')
        elif self.type == 'variable':
            return tags.div('', cls='node variable')
        elif self.type == 'answer':
            return tags.div('', cls='node answer')
        else:
            raise ValueError(f"Invalid node type: {self.type}")


class Chain:
    def __init__(self, nodes=[]):
        self.nodes = nodes
    
    def get_html(self):
        chain_html = tags.div('', cls='chain')
        for node in self.nodes:
            chain_html.add(node.get_html())
        return chain_html


class Map:
    def __init__(self, shape, chains=Chain(), name=None):
        self.shape = shape
        self.chains = chains
        self.name = name
    
    def get_html(self):
        map_html = f'<div class="map {self.shape}">'
        for chain in self.chains:
            chain_html = '<div class="chain">'
            for node in chain.nodes:
                node_html = f'<div class="node {node.type}"></div>'
                chain_html += node_html
            chain_html += '</div>'
            map_html += chain_html
        map_html += '</div>'
        return map_html
class Puzzle(Map):
    def __init__(self, shape, chains=[], name=None):
        super().__init__(shape, chains, name=name)
    
    def set_header_files(self):
        header_files = [
            'main.css'
        ]
        header_html = ''
        for file in header_files:
            header_html += f'<link rel="stylesheet" href="{file}">'
        return header_html
    
    def get_puzzle_html(self):
        puzzle_html = f'<html><head>{self.set_header_files()}</head><body><div class="puzzle {self.shape}">'
        nodes_by_value = {}
        for chain in self.chains:
            for node in chain.nodes:
                if node.type == 'number':
                    value = random.randint(1, 9)
                    if value not in nodes_by_value:
                        nodes_by_value[value] = []
                    nodes_by_value[value].append(node)
        
        for value, nodes in nodes_by_value.items():
            if len(nodes) > 1:
                puzzle_chain_html = '<div class="puzzle-chain">'
                for node in nodes:
                    node_html = f'<div class="puzzle-node {node.type}">{value}</div>'
                    puzzle_chain_html += node_html
                puzzle_chain_html += '</div>'
                puzzle_html += puzzle_chain_html
        
        puzzle_html += '</div></body></html>'
        return puzzle_html

# Define the minimum number of chains required for each map shape
MIN_CHAINS = {
    'triangle': 3,
    'square': 4,
    'hexagon': 6,
}

# Define the shapes available for the map
SHAPES = ['triangle', 'square', 'hexagon']

# Get user input for map shape and number of chains
shape = ''
while shape not in SHAPES:
    shape = input(f"Select a map shape ({', '.join(SHAPES)}): ")
num_chains = 0
while num_chains < MIN_CHAINS[shape]:
    num_chains = int(input(f"Enter the number of chains (minimum {MIN_CHAINS[shape]}): "))

# Generate random chains
chains = []
for i in range(num_chains):
    chain_length = random.randint(5, 10)
    nodes = []
    for j in range(chain_length):
        if j == 0:
            node_type = random.choice(['number', 'variable'])
        elif j == chain_length - 2:
            node_type = 'operator'
        elif j == chain_length - 1:
            node_type = 'answer'
        else:
            node_type = random.choice(['number', 'operator', 'variable'])
        nodes.append(Node(node_type))
    chains.append(Chain(nodes))


# Build the puzzle
puzzle_name = input("Enter a name for the puzzle: ")
puzzle_obj = Puzzle(shape, chains, name=puzzle_name)
puzzle_html = puzzle_obj.get_puzzle_html()

# Save the puzzle as an HTML file
filename = f"{puzzle_name}_{shape}_{num_chains}.html"

print(puzzle_html,file=open(filename,'w'))
