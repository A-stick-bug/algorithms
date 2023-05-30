# simpler implementation with heap, this is faster for sparse graphs
# if the nodes are numbers, a list can be used instead of a dict

import heapq


def shortest_path(start, end, graph):
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    parents = {node: None for node in graph}
    pq = [(0, start)]  # Create a priority queue (heap) with the starting node and its cost
    processed = set()  # Keep track of processed nodes

    while pq:  # Continue until the priority queue is empty
        cost, node = heapq.heappop(pq)  # Pop the node with the lowest cost from the priority queue
        if node in processed:
            continue

        neighbors = graph[node]  # Get the neighbors of the current node

        # Add a check to ensure neighbors is not None
        if neighbors is not None:
            for neighbor, neighbor_cost in neighbors:  # Iterate over the neighbors and their costs
                new_cost = cost + neighbor_cost  # Calculate the new cost to reach the neighbor through the current node
                if costs[neighbor] > new_cost:  # Update the cost if it is lower than the current cost
                    costs[neighbor] = new_cost
                    parents[neighbor] = node  # Update the parent of the neighbor to the current node
                    heapq.heappush(pq, (new_cost, neighbor))  # Push the updated cost and neighbor to the priority queue

        processed.add(node)
    return costs, parents


graph = {"start": [("a", 6), ("b", 2)],
         "a": [("fin", 1)],
         "b": [("a", 3), ("fin", 5)],
         "fin": None}

start = "start"
end = "fin"
result_costs, result_parents = shortest_path(start, end, graph)
print(f"Shortest path costs: {result_costs}")
print(f"Shortest path parents: {result_parents}")
