import networkx as nx


def next_lower_letter(char):
    if char not in ['z', 'Z']:
        return chr(ord(char.lower()) + 1)
    else:
        return 'z'


def create_graph(path):
    graph = nx.DiGraph()
    with open(path) as file:
        line_index = 1
        for line in file:
            line = line.replace('\n', '').replace('S', 'A').replace('E', 'Z')
            col_index = 1
            for char in line:
                graph.add_node(col_index+line_index*1j, altitude=char)
                col_index += 1
            line_index += 1
    return graph


def is_accessible(graph, node, other):
    return graph.has_node(other) and (graph.nodes[node]['altitude'].lower() >= graph.nodes[other]['altitude'].lower() or
                                      next_lower_letter(graph.nodes[node]['altitude']) ==
                                      graph.nodes[other]['altitude'].lower())


def add_edges(graph: nx.DiGraph):
    for node in graph.nodes:
        if is_accessible(graph, node, node - 1):
            graph.add_edge(node, node - 1)
        if is_accessible(graph, node, node + 1j):
            graph.add_edge(node, node + 1j)
        if is_accessible(graph, node, node + 1):
            graph.add_edge(node, node + 1)
        if is_accessible(graph, node, node - 1j):
            graph.add_edge(node, node - 1j)
    return graph


def find_shortest_path(path, multiple_starts=False):
    graph = create_graph(path)
    graph = add_edges(graph)
    if multiple_starts:
        start_nodes = [x for x, y in graph.nodes(data=True) if y['altitude'].lower() == 'a']
    else:
        start_nodes = [x for x, y in graph.nodes(data=True) if y['altitude'] == 'A']
    exit_node = [x for x, y in graph.nodes(data=True) if y['altitude'] == 'Z'][0]
    output = len(graph)
    for start_node in start_nodes:
        try:
            shortest_path = nx.shortest_path_length(graph, start_node, exit_node)
        except nx.NetworkXNoPath:
            continue
        if shortest_path < output:
            output = shortest_path
    return output
