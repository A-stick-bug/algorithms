def selection_sort(arr):
    size = len(arr)
    count = 0

    for index in range(size):
        min_index = index

        for j in range(index + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[index], array[min_index]) = (array[min_index], array[index])

        count += 1


array = [3, 1, 2]
selection_sort(array)

print(array)