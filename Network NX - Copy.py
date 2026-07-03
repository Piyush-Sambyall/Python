import networkx as nx
import matplotlib.pyplot as plt

# Function to create a graph and apply Dijkstra's Algorithm
def dijkstra_experiment():
    # Create a weighted graph
    G = nx.Graph()

    # Add edges and weights (can modify for different graphs)
    G.add_weighted_edges_from
    ([
        ('A', 'B', 4),
        ('A', 'C', 1),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3),
    ])
    
    # Apply Dijkstra's algorithm to find shortest paths from node 'A'
    source_node = 'A'
    shortest_paths = nx.single_source_dijkstra_path(G, source_node)
    shortest_distances = nx.single_source_dijkstra_path_length(G, source_node)

    # Print the shortest paths and their distances
    print(f"Shortest paths from {source_node}:")
    for target, path in shortest_paths.items():
        print(f"Path to {target}: {path}, Distance: {shortest_distances[target]}")

    # Visualize the graph with the shortest paths
    pos = nx.spring_layout(G)  # Layout for positioning nodes
    plt.figure(figsize=(8, 6))

    # Draw the nodes and edges
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color='gray')

    # Highlight the shortest paths by drawing them in red
    for target, path in shortest_paths.items():
        if path != [source_node]:  # Exclude the source node itself
            edges_in_path = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="red", width=2)

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Title and display
    plt.title(f"Shortest Paths from {source_node}")
    plt.show()

# Run the experiment
dijkstra_experiment()
