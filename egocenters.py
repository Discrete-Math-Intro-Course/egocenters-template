import networkx as nx

def find_impostor(edgelist, pseudocenters):
    imp_list = []
    deg_list = []
    for i in pseudocenters:
        imp_list += [item for item in edgelist if item[0] == i]
    graph = nx.Graph()
    graph.add_edges_from(imp_list)
    for j in pseudocenters:
        deg_list += [nx.degree(graph, j)]
    impostor = pseudocenters[deg_list.index(min(deg_list))]
    return impostor