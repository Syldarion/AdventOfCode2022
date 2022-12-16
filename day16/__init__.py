import re
from copy import deepcopy
from util import text_file_args


def build_edge_graph(lines):
    graph = {}
    for line in lines:
        line_data = re.match(r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w\s,]+)", line)
        origin = line_data.group(1)
        rate = int(line_data.group(2))
        destinations = line_data.group(3).split(", ")
        graph[origin] = {
            "rate": rate,
            "destinations": destinations,
            "distances": {},
            "is_open": False
        }

    all_origins = list(graph.keys())

    for origin in all_origins:
        graph[origin]["distances"] = djikstra(graph, origin)[1]

    return graph


def djikstra(graph, start_node):
    unvisited = list(graph.keys())
    shortest_path = {}
    previous_nodes = {}
    max_value = 999999999
    for node in unvisited:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited:
        current_smallest_node = None
        for node in unvisited:
            if not current_smallest_node or shortest_path[node] < shortest_path[current_smallest_node]:
                current_smallest_node = node
        destinations = graph[current_smallest_node]["destinations"]
        for destination in destinations:
            tentative_value = shortest_path[current_smallest_node] + 1
            if tentative_value < shortest_path[destination]:
                shortest_path[destination] = tentative_value
                previous_nodes[destination] = current_smallest_node
        unvisited.remove(current_smallest_node)

    return previous_nodes, shortest_path


@text_file_args
def part1(*args):
    graph = build_edge_graph(args[0])
    start_node = "AA"

    valve_bit = {}
    for i, location in enumerate(graph.keys()):
        valve_bit[location] = 1 << i

    for key, value in valve_bit.items():
        graph[value] = deepcopy(graph[key])

    valve_states = [(valve_bit[start_node], 0, 0)]
    best_state = {}

    for t in range(1, 31):
        new_states = []

        for location, opened, pressure in valve_states:
            state_key = (location, opened)
            if state_key in best_state and pressure <= best_state[state_key]:
                continue

            best_state[state_key] = pressure

            rate = graph[location]["rate"]
            destinations = graph[location]["destinations"]

            if location & opened == 0 and rate > 0:
                new_states.append((location, opened | location, pressure + rate * (30 - t)))
            for destination in destinations:
                new_states.append((valve_bit[destination], opened, pressure))

        valve_states = new_states

    print(max(pressure for _, _, pressure in valve_states))
