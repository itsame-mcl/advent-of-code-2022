import networkx as nx
from math import lcm
from collections import namedtuple

XYTCoordinates = namedtuple("XYTCoordinates", "x y t")
START = XYTCoordinates(x=-1, y=-1, t=-1)
GOAL = XYTCoordinates(x=-2, y=-2, t=-2)


def import_first_state_as_graph(path):
    graph = nx.DiGraph()
    graph.add_node(START, status='start')
    graph.add_node(GOAL, status='goal')
    with open(path) as file:
        lines = file.readlines()
    y = 0
    x_max = 0
    y_max = len(lines)-1
    for line in lines:
        line = line.replace('\n', '')
        x = 0
        for char in line:
            match[char, y]:
                case['.', _]:
                    graph.add_node(XYTCoordinates(x=x, y=y, t=0), status='land',
                                   wind={'^': False, '>': False, 'v': False, '<': False})
                case['^', _]:
                    graph.add_node(XYTCoordinates(x=x, y=y, t=0), status='blizzard',
                                   wind={'^': True, '>': False, 'v': False, '<': False})
                case['>', _]:
                    graph.add_node(XYTCoordinates(x=x, y=y, t=0), status='blizzard',
                                   wind={'^': False, '>': True, 'v': False, '<': False})
                case['v', _]:
                    graph.add_node(XYTCoordinates(x=x, y=y, t=0), status='blizzard',
                                   wind={'^': False, '>': False, 'v': True, '<': False})
                case['<', _]:
                    graph.add_node(XYTCoordinates(x=x, y=y, t=0), status='blizzard',
                                   wind={'^': False, '>': False, 'v': False, '<': True})
                case _:
                    pass  # If it's a wall, do nothing
            x += 1
        x_max = x-1
        y += 1
    return graph, x_max-1, y_max-1


def compute_to_modify(graph, node, x_max, y_max, direction):
    match direction:
        case '^':
            to_modify = XYTCoordinates(x=node.x, y=node.y - 1, t=node.t + 1) \
                        if XYTCoordinates(x=node.x, y=node.y - 1, t=node.t + 1) in graph.nodes \
                        else XYTCoordinates(x=node.x, y=y_max, t=node.t + 1)
        case 'v':
            to_modify = XYTCoordinates(x=node.x, y=node.y + 1, t=node.t + 1) \
                        if XYTCoordinates(x=node.x, y=node.y + 1, t=node.t + 1) in graph.nodes \
                        else XYTCoordinates(x=node.x, y=1, t=node.t + 1)
        case '>':
            to_modify = XYTCoordinates(x=node.x + 1, y=node.y, t=node.t + 1) \
                        if XYTCoordinates(x=node.x + 1, y=node.y, t=node.t + 1) in graph.nodes \
                        else XYTCoordinates(x=1, y=node.y, t=node.t + 1)
        case _:
            to_modify = XYTCoordinates(x=node.x - 1, y=node.y, t=node.t + 1) \
                        if XYTCoordinates(x=node.x - 1, y=node.y, t=node.t + 1) in graph.nodes \
                        else XYTCoordinates(x=x_max, y=node.y, t=node.t + 1)
    return to_modify


def compute_state(graph, x_max, y_max, t):
    current_state_nodes = [node for node in graph.nodes if node.t == t]
    # Create next state nodes
    for node in current_state_nodes:
        new_node = XYTCoordinates._replace(node, t=t + 1)
        graph.add_node(new_node, status='land',
                       wind={'^': False, '>': False, 'v': False, '<': False})
    # Modify next state nodes, based on wind
    for node in current_state_nodes:
        wind = graph.nodes[node]['wind']
        if wind['^']:
            to_modify = compute_to_modify(graph, node, x_max, y_max, '^')
            graph.nodes[to_modify]['status'] = 'blizzard'
            graph.nodes[to_modify]['wind']['^'] = True
        if wind['v']:
            to_modify = compute_to_modify(graph, node, x_max, y_max, 'v')
            graph.nodes[to_modify]['status'] = 'blizzard'
            graph.nodes[to_modify]['wind']['v'] = True
        if wind['>']:
            to_modify = compute_to_modify(graph, node, x_max, y_max, '>')
            graph.nodes[to_modify]['status'] = 'blizzard'
            graph.nodes[to_modify]['wind']['>'] = True
        if wind['<']:
            to_modify = compute_to_modify(graph, node, x_max, y_max, '<')
            graph.nodes[to_modify]['status'] = 'blizzard'
            graph.nodes[to_modify]['wind']['<'] = True
    return graph


def compute_other_states(graph, x_max, y_max):
    number_of_states = lcm(x_max, y_max)
    for t in range(number_of_states-1):
        graph = compute_state(graph, x_max, y_max, t)
    return graph, number_of_states


def add_edges_to_graph(graph, states, y_max):
    for node in graph.nodes:
        if node in [START, GOAL]:
            continue
        wait = XYTCoordinates(x=node.x, y=node.y, t=(node.t + 1) % states)
        up = XYTCoordinates(x=node.x, y=node.y - 1, t=(node.t + 1) % states)
        down = XYTCoordinates(x=node.x, y=node.y + 1, t=(node.t + 1) % states)
        left = XYTCoordinates(x=node.x - 1, y=node.y, t=(node.t + 1) % states)
        right = XYTCoordinates(x=node.x + 1, y=node.y, t=(node.t + 1) % states)
        for option in [wait, up, down, left, right]:
            if option in graph.nodes and graph.nodes[option]['status'] == 'land':
                graph.add_edge(node, option)
        if node.y == 0:
            graph.add_edge(node, START)
        if node.y == y_max + 1:
            graph.add_edge(node, GOAL)
    return graph


def find_shortest_path(path, multi_trip=False):
    graph, x_max, y_max = import_first_state_as_graph(path)
    graph, states = compute_other_states(graph, x_max, y_max)
    graph = add_edges_to_graph(graph, states, y_max)
    first_start = [node for node in graph.nodes if node.y == 0 and node.t == 0][0]
    first_trip = nx.shortest_path_length(graph, first_start, GOAL) - 1
    if not multi_trip:
        return first_trip
    second_start = [node for node in graph.nodes if node.y == y_max + 1 and node.t == (first_trip % states)][0]
    second_trip = nx.shortest_path_length(graph, second_start, START) - 1
    third_start = [node for node in graph.nodes if node.y == 0 and node.t == (first_trip+second_trip) % states][0]
    third_trip = nx.shortest_path_length(graph, third_start, GOAL) - 1
    return first_trip + second_trip + third_trip
