import networkx as nx


def gl_find(gr, str, visited):
    # if str == fns:
    #     return True
    visited[str] = True
    #print(visited)
    print(str, gr.adj[str])
    # проход по графу
    for node in gr.adj[str]:
        if not visited[node]:  # если не посещали узел
            gl_find(gr, node, visited)

    return None

if __name__ == "__main__":
    gr = nx.Graph()
    gr.add_nodes_from("ABCDEFG")
    gr.add_edges_from(
        [
            ('A', 'B'),
            ('B', 'C'),
            ('C', 'D'),
            ('F', 'G')
        ]
    )

    visited = {node: False for node in gr.nodes()}
    num = 0
    for node in gr.adj:
        if not visited[node]:  # если не посещали узел
            gl_find(gr, node, visited)
            num += 1
            print("-----")
    print(num)