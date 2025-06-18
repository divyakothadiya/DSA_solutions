def merge(arr, start, mid, end):
    temp = []
    i = start
    j = mid + 1

    # Merge two sorted halves
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Copy remaining elements of left half
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Copy remaining elements of right half
    while j <= end:
        temp.append(arr[j])
        j += 1

    # Copy temp back into original array
    for k in range(len(temp)):
        arr[start + k] = temp[k]

def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(arr, start, mid)       # left half
        mergesort(arr, mid + 1, end)     # right half
        merge(arr, start, mid, end)

if __name__ == "__main__":
    data = [15, 32, 60, 44, 11, 39]
    mergesort(data, 0, len(data) - 1)
    print("Sorted:", data)
