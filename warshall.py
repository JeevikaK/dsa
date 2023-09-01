def warshall(arr, n):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = max(arr[i][j], arr[i][k] and arr[k][j])

def main():
    arr = [[0 for _ in range(10)] for _ in range(10)]
    print("enter number of vertices")
    n = int(input())
    print("enter number of edges")
    e = int(input())
    for i in range(e):
        print("enter vertices of edge", i)
        u = int(input())
        v = int(input())
        arr[u][v] = 1
    warshall(arr, n)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end="")
        print()

main()