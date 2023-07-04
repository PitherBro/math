import math
from dominate import tags


class Node:
    def __init__(self, value):
        self.value = value

    def get_html(self):
        return tags.div(self.value, cls='node')

class Operator(Node):
    def __init__(self, value):
        super().__init__(value)

    def get_html(self):
        return tags.div(self.value, cls='operator')

class Chain:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_html(self):
        nodes_html = [node.get_html() for node in self.nodes]
        return tags.div(*nodes_html, cls='chain')

class Map:
    SHAPES = {
        'triangle': [(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)],
        'square': [(0, 0), (1, 0), (1, 1), (0, 1)],
        'hexagon': [(0, 0.5), (0.25, 0.25), (0.75, 0.25), (1, 0.5),
                    (0.75, 0.75), (0.25, 0.75)]
    }

    def __init__(self, chains):
        self.chains = chains

    def get_html(self, num_nodes):
        total_nodes = sum(len(chain.nodes) for chain in self.chains)
        if total_nodes != num_nodes:
            raise ValueError(f'Number of nodes {num_nodes} does not match '
                             f'total number of nodes in chains {total_nodes}')
        shape = self.SHAPES.get('hexagon')
        scale = int(math.ceil(math.sqrt(num_nodes / len(shape))))
        width = scale * 2
        height = int(math.ceil(num_nodes / (width * len(shape))) * 2)
        nodes_html = [node.get_html() for chain in self.chains for node in chain.nodes]
        nodes_html += [tags.div(cls='empty-node') for _ in range(num_nodes - total_nodes)]
        map_html = tags.div(*nodes_html, cls='map')
        map_html['style'] = f'width: {width}em; height: {height}em;'
        return map_html


# create chains
chain1 = Chain([Node(1), Operator('+'), Node(2), Operator('*'), Node(3)])
chain2 = Chain([Node(4), Operator('-'), Node(2), Operator('/'), Node(2)])
chain2 = Chain([Node(4), Operator('-'), Node(), Operator('/'), Node(2)])
chains = [chain1, chain2]

# create map and display
num_nodes = 15
map = Map(chains)
map_html = map.get_html(num_nodes)
print(map_html.render())
