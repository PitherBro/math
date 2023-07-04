from typing import List
from dominate import tags as tg
import random

class Node:
    def __init__(self, value: str, html_tag: str, html_attrs: dict):
        self.value = value
        self.html_tag = html_tag
        self.html_attrs = html_attrs

    def get_html(self):
        html_node = tg.__getattr__(self.html_tag)(self.value)
        for attr, value in self.html_attrs.items():
            html_node.attrs[attr] = value
        return html_node


class Operator(Node):
    def __init__(self, value: str):
        html_tag = 'td'
        html_attrs = {'colspan': '2'}
        super().__init__(value, html_tag, html_attrs)


class Number(Node):
    def __init__(self, value: str):
        html_tag = 'td'
        html_attrs = {'rowspan': '2'}
        super().__init__(value, html_tag, html_attrs)


class Equals(Node):
    def __init__(self, value: str):
        html_tag = 'td'
        html_attrs = {'rowspan': '2'}
        super().__init__(value, html_tag, html_attrs)


class Chain:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    def get_html(self):
        html_chain = tg.tr()
        for node in self.nodes:
            html_node = node.get_html()
            html_chain += html_node
        return html_chain


class Map:
    def __init__(self, shape: str, chains: List[Chain]):
        self.shape = shape
        self.chains = chains

    def get_html(self):
        html_map = tg.div()
        for chain in self.chains:
            html_chain = chain.get_html()
            html_map += html_chain
        return html_map.render()

    def save_html(self, filename: str):
        with open(filename, 'w') as f:
            f.write(self.get_html())

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

# Build the map
map_name = input("Enter a name for the map: ")
map_obj = Map(shape, chains, name=map_name)
map_html = map_obj.get_html()

# Save the map as an HTML file
filename = f"{map_name}_{shape}_{num_chains}.html"
