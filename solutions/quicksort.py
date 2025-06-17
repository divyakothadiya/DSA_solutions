def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

def quicksort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1) #left partition
        quicksort(arr, pivot_index + 1, end)  #right partition

if __name__ == "__main__":
    data = [15, 32, 60, 44, 11, 39]
    quicksort(data, 0, len(data) - 1)
    print("Sorted:", data)
