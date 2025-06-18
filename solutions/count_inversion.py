#1st solution using brute force, time complexity=O(n^2)
def bruteforce(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                count += 1
    return count

#2nd & optimal solution using merge sort, time complexity=O(nlogn) hence its optimal solution for count inversion
def merge(arr, start, mid, end):
    temp = []
    i = start
    j = mid + 1
    invCount=0

    # Merge two sorted halves
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            invCount += mid-i+1

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
        
    return invCount

def mergesort(arr, start, end):
    
    if start < end:
        mid = (start + end) // 2
        leftInvCount = mergesort(arr, start, mid)       # left half
        rightInvCount = mergesort(arr, mid + 1, end)     # right half
        invCount = merge(arr, start, mid, end)
        return leftInvCount+rightInvCount+invCount
    else:    
        return 0

if __name__ == "__main__":
    data = [15, 32, 60, 44, 11, 39]
    count=mergesort(data, 0, len(data) - 1)
    data = [15, 32, 60, 44, 11, 39]
    invcount=bruteforce(data)
    print("Inversion count using brute force:", invcount)
    print("Inversion count using merge sort:", count)
