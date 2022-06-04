import networkx as nx

G = nx.Graph()

edges = [(1, 2, 19), (1, 6, 15), (2, 3, 6), (2, 4, 10),
		(2, 6, 22), (3, 4, 51), (3, 5, 14), (4, 8, 20),
		(4, 9, 42), (6, 7, 30)]

G.add_weighted_edges_from(edges)
nx.draw_networkx(G)

print("Total number of nodes: ", int(G.number_of_nodes()))
print("Total number of edges: ", int(G.number_of_edges()))
print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges()))
print("Degree for all nodes: ", dict(G.degree))

# print("Total number of self-loops: ", int(G.number_of_selfloops()))
# print("List of all nodes with self-loops: ", list(G.nodes_with_selfloops()))

print("List of all nodes we can go to in a single step from node 2: ", list(G.neighbors(2)))
