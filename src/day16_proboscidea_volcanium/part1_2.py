import networkx as nx
from re import findall, search
from itertools import combinations


def create_graph(path):
    graph = nx.Graph()
    edges = list()
    with open(path) as file:
        for line in file:
            valves = findall(r'[A-Z]{2}', line)
            rate = search(r'\d+', line).group()
            graph.add_node(valves[0], rate=int(rate))
            edges.extend([(valves[0], other) for other in valves[1:]])
    graph.add_edges_from(edges)
    return graph


def explore_all_options(start, current_releasing, total_pressure, available_valves, distances, remaining_time):
    final_pressure = total_pressure + current_releasing * remaining_time
    max_final_pressure = final_pressure
    if available_valves:
        for valve in available_valves:
            moving_and_opening_time = distances[start][valve[0]] + 1
            if moving_and_opening_time < remaining_time:
                new_remaining_time = remaining_time - moving_and_opening_time
                new_total_pressure = total_pressure + current_releasing * moving_and_opening_time
                new_releasing = current_releasing + valve[1]
                new_available_valves = available_valves[:]
                new_available_valves.remove(valve)
                possible_final_pressure = explore_all_options(valve[0], new_releasing, new_total_pressure,
                                                              new_available_valves, distances,
                                                              new_remaining_time)
                if possible_final_pressure > max_final_pressure:
                    max_final_pressure = possible_final_pressure
    return max_final_pressure


def release_most_pressure(path, elephant=False):
    graph = create_graph(path)
    distances = dict(nx.shortest_path_length(graph))
    valves = [(node[0], node[1]['rate']) for node in graph.nodes.data() if node[1]['rate'] > 0]
    if not elephant:
        max_final_pressure = explore_all_options("AA", 0, 0, valves, distances, 30)
    else:
        max_final_pressure = 0
        for number_of_valves_for_elephant in range(1, len(valves)//2+1):
            valves_for_elephant_comb = combinations(valves, number_of_valves_for_elephant)
            for valves_for_elephant in valves_for_elephant_comb:
                valves_for_elephant = [*valves_for_elephant]
                max_final_pressure_elephant = explore_all_options("AA", 0, 0, valves_for_elephant, distances, 26)
                valves_for_human = [valve for valve in valves if valve not in valves_for_elephant]
                max_final_pressure_human = explore_all_options("AA", 0, 0, valves_for_human, distances, 26)
                if (max_final_pressure_elephant + max_final_pressure_human) > max_final_pressure:
                    max_final_pressure = max_final_pressure_elephant + max_final_pressure_human
    return max_final_pressure
