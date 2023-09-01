def quicksort(arr, first, last):
    if first < last:
        pivot = first  # Selecting the middle element as the pivot
        i = first
        j = last
        while i <= j:
            while arr[i] < arr[pivot]:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        quicksort(arr, first, j)
        quicksort(arr, i, last)

arr = [2, 4, 6, 1, 3, 9, 8, 7]
quicksort(arr, 0, len(arr) - 1)
print(arr)