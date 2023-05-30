from collections import deque


def bfs(graph, target, start):
    used = set()
    search_queue = deque()
    search_queue += graph[start]

    while search_queue:
        person = search_queue.popleft()
        if person not in used:
            if person == target:
                return f"{target} is in the graph"
            else:
                search_queue += graph[person]
                used.add(person)

    return f"{target} is not in the graph"


graph = {"start": ["a", "b"], "a": ["d", "e"], "b": [], "d": [], "e": []}
print(bfs(graph, "d", "start"))


# slight modifications
# def bfs(graph, target, start):
#     used = set()
#     search_queue = deque()
#     search_queue += graph[start]
#
#     while search_queue:
#         person = search_queue.popleft()
#         if person == target:
#             return f"{target} is in the graph"
#         else:
#             for i in graph[person]:
#                 if i not in used:
#                     search_queue.append(i)
#             used.add(person)
#
#     return f"{target} is not in the graph"
