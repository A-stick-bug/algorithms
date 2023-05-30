from collections import deque
from numpy import matrix


def search(grid, start, target):
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
    distances = [[float("inf") for _ in range(len(grid))] for _ in range(len(grid[0]))]
    distances[start[0]][start[1]] = 0

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    to_search = deque([start])
    ROWS, COLS = len(grid), len(grid[0])

    while to_search:
        cell = to_search.popleft()
        row = cell[0]
        col = cell[1]
        if not grid[row][col]:
            if cell == target:
                # too lazy to format
                print(matrix(distances))
                return f"Target is {distances[target[0]][target[1]]} from start."

            visited[row][col] = True

            # adding adjacent
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                if 0 <= new_c < COLS and 0 <= new_r < ROWS and grid[new_r][new_c] == 0:
                    to_search.append((new_r, new_c))
                    if distances[new_r][new_c] > distances[row][col] + 1:
                        distances[new_r][new_c] = distances[row][col] + 1
    return "Path not found"


grid = [[1, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 0]]

start = (0, 1)
end = (3,3)
print(search(grid, start, end))
