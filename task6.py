import networkx as nx

orders = [(9, 12), (12, 15), (15, 16)]
a = True
graph = nx.MultiDiGraph()
graph.add_nodes_from(range(0, 23))
for order in orders:
    for i in range(order[0], order[1]):
        graph.add_edge(i, i+1)
for d in graph.out_degree:
    if d[1] > 1:
        a = False
        break
print(a)