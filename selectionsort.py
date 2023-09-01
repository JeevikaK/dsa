def selection(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

arr = [2, 4, 7, 1, 3, 9, 8]
selection(arr)
print(arr)