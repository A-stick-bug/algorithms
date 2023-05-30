# V^2, good for dense graphs

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[start] = 0

    for _ in range(n):
        min_distance = float('inf')
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                u = i
                min_distance = distances[i]
        visited[u] = True

        for k in range(n):
            if not visited[k] and graph[u][k] and (distances[u] + graph[u][k] < distances[k]):
                distances[k] = distances[u] + graph[u][k]
    return distances


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print(dijkstra(graph, 0))
