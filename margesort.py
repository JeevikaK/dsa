def combine(arr, low, mid, high):
    temp = []
    i = low
    j = mid+1
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i - low]

def mergesort(arr, low, high):
    if low < high-1:
        mid = low + (high - low) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        combine(arr, low, mid, high)


arr = [2, 5, 6, 8, 1, 3, 10]
mergesort(arr, 0, len(arr)-1)
print(arr)