#Plot Graphs
'''
This module just focuses on loading a set
of json files from folder 'saves'
once all files are loaded they are graphed.
'''
import matplotlib.pyplot as plt
from commonData import *

'''
plots a single graph using python's built in lib pyplot
graphs follow a Name, #steps taken, and each step Results
'''
def plot_graph(saveObj):
    """
    Plots a graph with the given name, number of steps, and results.
    """
    num_steps = saveObj['#steps']
    results = saveObj['list']
    name = saveObj['number']
    
    plt.plot(range(num_steps), results)
    plt.xlabel('Steps')
    plt.ylabel('Values')
    plt.title(f'Graph {name}')
    plt.show()
'''
plots multiple graphs using pyplot
same fields except this one take s a list of graph objs
'''
def plot_graphs(saveObjs):
    """
    Plots multiple graphs with the given names, number of steps, and results as subplots.
    """
    num_graphs = len(saveObjs)
    num_rows = int(num_graphs / 2) + num_graphs % 2
    num_cols = 2 if num_graphs > 1 else 1
    
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(8, 6))
    
    for i, saveObj in enumerate(saveObjs):
        num_steps = saveObj['#steps']
        results = saveObj['list']
        name = saveObj['number']
        
        row = i // num_cols
        col = i % num_cols
        
        if num_graphs == 1:
            ax = axs
        elif num_rows == 1:
            ax = axs[col]
        else:
            ax = axs[row, col]
            
        ax.plot(range(num_steps), results)
        ax.set_xlabel('Steps')
        ax.set_ylabel('Values')
        ax.set_title(f'Graph {name}')
    
    plt.tight_layout()
    plt.show()
'''
scans the Saves directory and returns a list of graph files
'''
def loadGraphs():
    return os.listdir(savePath)

files = loadGraphs()
graphs = []


print(files)
for f in files:
    #print(f)
    obj = dict(json.load(open(savePath/f)))
    #print(obj)
    graphs.append(obj)

# Example usage
#plot_graphs(graphs)
