import heapq


def heapsort(arr):
    heapq.heapify(arr)
    res = []
    while arr:
        res.append(heapq.heappop(arr))
    return res

    # shorthand: return [heapq.heappop(arr) for _ in range(len(arr))]


numbers = [1,8,3,0,2,-6,1,4]
print(heapsort(numbers))
