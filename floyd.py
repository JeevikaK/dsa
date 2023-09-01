def floyd(arr):
    for k in range(0, len(arr)):
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], " ", end="")
        print()

arr = [[1, 2, 9], [5, 1, 9], [1, 5, 9]]
floyd(arr)