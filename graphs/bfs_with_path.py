from collections import deque


def bfs(graph, start, end):
    queue = deque([start])
    visited = set()
    distance = {start: 0}
    parents = {node: None for node in graph}

    while queue:
        node = queue.popleft()

        # target reached
        if node == end:
            print_path(parents, start, end)
            return distance[node]
        visited.add(node)

        # update parents and distance values for all neighbours
        # for regular bfs, we would simply add the neighbours to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

                # default dict could be used
                if neighbor in distance.keys():
                    if distance[neighbor] > distance[node] + 1:
                        distance[neighbor] = distance[node] + 1
                        parents[neighbor] = node
                else:
                    distance[neighbor] = distance[node] + 1
                    parents[neighbor] = node


def print_path(parents, start, end):
    path = [end]
    node = parents[end]
    while node != start:
        path.append(node)
        node = parents[node]
    path.append(node)
    print(*path[::-1], sep=" -> ")


graph = {"start": ["a", "b"], "a": ["d", "e"], "b": ["e"], "d": ["e"], "e": ["f"]}
print(bfs(graph, "start", "f"))
