# Import required libraries
import random
from typing import List, Tuple
import random


class MathPuzzle:
    def __init__(self, node_size: int, difficulty: str, node_shape: type, grid_shape: Tuple[int, int]):
        self.node_size = node_size
        self.difficulty = difficulty
        self.node_shape = node_shape()
        self.grid = Grid(grid_shape[0], grid_shape[1])
        self.chain_length = 3
        
        # Initialize visible nodes based on difficulty level
        self.visible_nodes = []
        if self.difficulty == "easy":
            self.visible_nodes = [0, 4, 8, 12]
        elif self.difficulty == "medium":
            self.visible_nodes = [0, 3, 5, 8, 10, 12]
        elif self.difficulty == "hard":
            self.visible_nodes = [0, 2, 4, 6, 8, 10, 12]
        elif self.difficulty == "insane":
            self.visible_nodes = [0, 2, 4, 6, 8, 9, 10, 12, 14]
        
        # Generate random map
        self.generate_random_map()
    
    def generate_random_map(self):
        # Get list of all possible node chains
        all_chains = self.get_all_chains()
        
        # Choose random chains to use
        chains = random.sample(all_chains, len(all_chains) // 2)
        
        # Place chains on grid
        for chain in chains:
            for i in range(len(chain)):
                row, col = chain[i]
                if self.grid.get_node(row, col) is None:
                    if i == 2:
                        value = chain[0][2] + chain[1][2]
                        node = Node(value, self.node_shape)
                    else:
                        node = Node(None, self.node_shape)
                    self.grid.set_node(row, col, node)
    
    def get_all_chains(self) -> List[List[Tuple[int, int, int]]]:
        chains = []
        empty_nodes = self.grid.get_empty_nodes()
        
        for node in empty_nodes:
            # Check if node has valid chains
            chain_indexes = self.get_chain_indexes_for_node(node)
            if len(chain_indexes) > 0:
                # Add all chains to list
                for chain in chain_indexes:
                    chains.append(chain)
        
        return chains
    
    def get_chain_indexes_for_node(self, node: Tuple[int, int]) -> List[List[Tuple[int, int, int]]]:
        row, col = node
        node_values = []
        neighbors = self.grid.get_valid_neighbors(row, col)
        for neighbor in neighbors:
            if self.grid.get_node(neighbor[0], neighbor[1]) is not None:
                node_values.append((neighbor[0], neighbor[1], self.grid.get_node(neighbor[0], neighbor[1]).value))
        
        chain_indexes = []
        for i in range(len(node_values)):
            for j in range(i + 1, len(node_values)):
                for k in range(j + 1, len(node_values)):
                    if node_values[i][2] == node_values[j][2] and node_values[j][2] == node_values[k][2]:
                        chain_indexes.append([node_values[i], node_values[j], node_values[k]])
        
        return chain_indexes
    

# Define node shapes
class Square:
    def __init__(self):
        self.shape = "square"
        
class Triangle:
    def __init__(self):
        self.shape = "triangle"
        
class Circle:
    def __init__(self):
        self.shape = "circle"

# Define Grid class
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for row in range(height):
            self.grid.append([])
            for col in range(width):
                self.grid[row].append(None)
                
    def set_node(self, row, col, node):
        self.grid[row][col] = node
        
    def get_node(self, row, col):
        return self.grid[row][col]
    
    def is_valid_location(self, row, col):
        return row >= 0 and row < self.height and col >= 0 and col < self.width
    
    def get_valid_neighbors(self, row, col):
        neighbors = []
        if self.is_valid_location(row - 1, col):
            neighbors.append((row - 1, col))
        if self.is_valid_location(row + 1, col):
            neighbors.append((row + 1, col))
        if self.is_valid_location(row, col - 1):
            neighbors.append((row, col - 1))
        if self.is_valid_location(row, col + 1):
            neighbors.append((row, col + 1))
        return neighbors
    
    def get_empty_nodes(self):
        empty_nodes = []
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is None:
                    empty_nodes.append((row, col))
        return empty_nodes

# Define node shape class definitions
class NodeShape:
    def __init__(self):
        self.shape = None
        
    def __str__(self):
        return self.shape

class Heart(NodeShape):
    def __init__(self):
        self.shape = "heart"
        
class Star(NodeShape):
    def __init__(self):
        self.shape = "star"
        
class Diamond(NodeShape):
    def __init__(self):
        self.shape = "diamond"
        
# Define bDefs class list
bDefs = [Square, Triangle, Circle, Grid, NodeShape, Heart, Star, Diamond]

# Define main function
def main():
    # Prompt user for options to build the map
    print("Welcome to the Math Puzzle Game!")
    node_size = int(input("Enter the size of each node (must be divisible by 3): "))
    difficulty = input("Enter difficulty level (easy, medium, hard, or insane): ")
    save_name = input("Enter a name to save the map: ")
    
    # Create MathPuzzle object
    math_puzzle = MathPuzzle(node_size, difficulty)
    
    # Generate random map
    math_puzzle.generate_random_map()
    
    # Show map
    math_puzzle.show_map()
    
    # Save map as HTML file
    math_puzzle.save_map_as_html(save_name)

main()