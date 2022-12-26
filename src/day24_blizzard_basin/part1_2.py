import networkx as nx
from math import lcm

START = -1-1j
GOAL = -2-2j


def create_graph_nodes(path):
    graph = nx.DiGraph()
    nodes = [(START, {'status': 'start'}), (GOAL, {'status': 'goal'})]
    with open(path) as file:
        lines = file.readlines()
    x_max = len(lines[0]) - 3
    y_max = len(lines) - 2
    states = lcm(x_max, y_max)
    position = 0
    for line in lines:
        line = line.replace('\n', '')
        for char in line:
            match char:
                case '.':
                    nodes.append((position+0j, {'status': 'land',
                                                'wind': {'^': False, '>': False, 'v': False, '<': False}}))
                case '^':
                    nodes.append((position+0j, {'status': 'blizzard',
                                                'wind': {'^': True, '>': False, 'v': False, '<': False}}))
                case '>':
                    nodes.append((position+0j, {'status': 'blizzard',
                                                'wind': {'^': False, '>': True, 'v': False, '<': False}}))
                case 'v':
                    nodes.append((position+0j, {'status': 'blizzard',
                                                'wind': {'^': False, '>': False, 'v': True, '<': False}}))
                case '<':
                    nodes.append((position+0j, {'status': 'blizzard',
                                                'wind': {'^': False, '>': False, 'v': False, '<': True}}))
                case _:
                    continue  # If it's a wall, do nothing
            for state in range(1, states):
                nodes.append((position + state*1j, {'status': 'land',
                                                    'wind': {'^': False, '>': False, 'v': False, '<': False}}))
            position += 1
    graph.add_nodes_from(nodes)
    return graph, x_max, y_max, states


def get_to_modify(node: complex, x_max, y_max, direction):
    match direction:
        case '^':
            to_modify = (node.real-x_max+(node.imag+1)*1j) \
                        if node.real > x_max \
                        else (x_max*y_max-(x_max-node.real)+(node.imag+1)*1j)
        case 'v':
            to_modify = (node.real+x_max+(node.imag+1)*1j) \
                        if node.real <= x_max * (y_max-1) \
                        else (node.real-(x_max*(y_max-1))+(node.imag+1)*1j)
        case '>':
            to_modify = (node.real+1+(node.imag+1)*1j) \
                        if node.real % x_max != 0 \
                        else (node.real-(x_max-1)+(node.imag+1)*1j)
        case _:
            to_modify = (node.real-1+(node.imag+1)*1j) \
                        if node.real % x_max != 1 \
                        else (node.real+(x_max-1)+(node.imag+1)*1j)
    return to_modify


def compute_blizzard(graph, x_max, y_max, states):
    for t in range(states-1):
        for x in range(0, x_max * y_max + 2):
            node = x + t * 1j
            wind = graph.nodes[node]['wind']
            if wind['^']:
                to_modify = get_to_modify(node, x_max, y_max, '^')
                graph.nodes[to_modify]['status'] = 'blizzard'
                graph.nodes[to_modify]['wind']['^'] = True
            if wind['v']:
                to_modify = get_to_modify(node, x_max, y_max, 'v')
                graph.nodes[to_modify]['status'] = 'blizzard'
                graph.nodes[to_modify]['wind']['v'] = True
            if wind['>']:
                to_modify = get_to_modify(node, x_max, y_max, '>')
                graph.nodes[to_modify]['status'] = 'blizzard'
                graph.nodes[to_modify]['wind']['>'] = True
            if wind['<']:
                to_modify = get_to_modify(node, x_max, y_max, '<')
                graph.nodes[to_modify]['status'] = 'blizzard'
                graph.nodes[to_modify]['wind']['<'] = True
    return graph


def get_next_options(node, x_max, y_max, states):
    wait = (node.real + ((node.imag + 1) % states) * 1j)
    up = (node.real - x_max + ((node.imag + 1) % states) * 1j) if node.real > x_max else None
    down = (node.real + x_max + ((node.imag + 1) % states) * 1j) if node.real <= x_max * (y_max - 1) else None
    left_or_start = (node.real - 1 + ((node.imag + 1) % states) * 1j) if\
        node.real % x_max != 1 or node.real == 1 else None
    right_or_goal = (node.real + 1 + ((node.imag + 1) % states) * 1j) if\
        node.real % x_max != 0 or node.real == x_max * y_max else None
    return wait, up, down, left_or_start, right_or_goal


def add_edges_to_graph(graph, x_max, y_max, states):
    edges = []
    for node in graph.nodes:
        if node in [START, GOAL]:
            continue
        if node.real == 0:
            edges.extend([(node, (node.real + 1 + ((node.imag + 1) % states) * 1j)), (node, START)])
        elif node.real == (x_max * y_max) + 1:
            edges.extend([(node, (node.real - 1 + ((node.imag + 1) % states) * 1j)), (node, GOAL)])
        else:
            options = get_next_options(node, x_max, y_max, states)
            for option in options:
                if option and graph.nodes[option]['status'] == 'land':
                    edges.append((node, option))
    graph.add_edges_from(edges)
    return graph


def find_shortest_path(path, trips=1):
    graph, x_max, y_max, states = create_graph_nodes(path)
    graph = compute_blizzard(graph, x_max, y_max, states)
    graph = add_edges_to_graph(graph, x_max, y_max, states)
    total_time = 0
    for trip in range(trips):
        origin = (0 if trip % 2 == 0 else x_max*y_max+1) + (total_time % states)*1j
        destination = GOAL if trip % 2 == 0 else START
        total_time += nx.shortest_path_length(graph, origin, destination) - 1
    return total_time
