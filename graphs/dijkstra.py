# implementation without the heap, faster if used with adjacency matrix


def shortest_path(start, graph):
    def find_lowest_cost_node():
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    costs = {node: float('inf') for node in graph}
    costs[start] = 0

    parents = {node: None for node in graph}
    processed = set()
    node = find_lowest_cost_node()

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        if neighbors is not None:
            for neighbor, neighbor_cost in neighbors:
                new_cost = cost + neighbor_cost
                if costs[neighbor] > new_cost:
                    costs[neighbor] = new_cost
                    parents[neighbor] = node
        processed.add(node)
        node = find_lowest_cost_node()
    return costs


# example to test code
graph = {"start": [("a", 6), ("b", 2)],
         "a": [("fin", 1)],
         "b": [("a", 3), ("fin", 5)],
         "fin": None}

print(shortest_path("start", graph))
