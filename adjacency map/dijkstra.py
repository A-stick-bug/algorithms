def shortest_path(start, end, graph):
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

    # to stop once the end node is reached, remove to test shortest distance to all points
    if node == end:
        return costs[end]

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        # Add a check to ensure neighbors is not None
        if neighbors is not None:
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]

                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node()
    return costs


# example to test code
graph = {"start": {"a": 6, "b": 2},
         "a": {"fin": 1},
         "b": {"a": 3, "fin": 5},
         "fin": None}

print(shortest_path("start", "fin", graph))
