import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph representing the map of Thailand
G = nx.Graph()

# Adding cities and distances
cities = {
    'Bangkok': (100, 200),
    'Chiang Mai': (400, 400),
    'Phuket': (300, 100),
    'Pattaya': (150, 250),
    'Krabi': (250, 50)
}

for city, pos in cities.items():
    G.add_node(city, pos=pos)

# Adding edges with distances
edges = [('Bangkok', 'Chiang Mai', 800),
         ('Bangkok', 'Phuket', 900),
         ('Bangkok', 'Pattaya', 150),
         ('Bangkok', 'Krabi', 700),
         ('Chiang Mai', 'Phuket', 1200),
         ('Chiang Mai', 'Pattaya', 1100),
         ('Chiang Mai', 'Krabi', 900),
         ('Phuket', 'Pattaya', 1200),
         ('Phuket', 'Krabi', 400),
         ('Pattaya', 'Krabi', 800)]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Function to calculate total distance for a given path
def total_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i+1]]['weight']
    distance += graph[path[-1]][path[0]]['weight']
    return distance

# Brute-force approach to find the shortest path
def brute_force_tsp(graph, start, destination):
    all_paths = list(itertools.permutations(graph.nodes()))
    min_distance = float('inf')
    min_path = None

    for path in all_paths:
        if path[0] == start and path[-1] == destination:
            distance = total_distance(path, graph)
            if distance < min_distance:
                min_distance = distance
                min_path = path

    return min_path, min_distance

# Input start and destination cities
start_city = 'Bangkok'
destination_city = 'Chiang Mai'

# Find and print the shortest path
shortest_path, shortest_distance = brute_force_tsp(G, start_city, destination_city)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)

# Draw the map with the shortest path highlighted
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)] + [(shortest_path[-1], shortest_path[0])], edge_color='r', width=2)
plt.show()
