def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while high >= low:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


arr = [1, 5, 6, 12, 23, 67, 78, 80]
x = 80

result = binary_search(arr, x)

print(result)
