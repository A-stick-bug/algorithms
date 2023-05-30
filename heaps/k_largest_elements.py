# classic heap problem, this solution is O(N*logK)
import heapq


def findKElements(nums, k):
    heap = nums[:k]
    for i in range(k, len(nums)):
        heapq.heappushpop(heap, nums[i])  # an alternative is testing if nums[i] > heap[0]: use heapreplace()
    return heap


print(findKElements([1, 2, 7, 2, 5, 7, 26, 25, 1], 3))
