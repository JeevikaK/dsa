def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal():
    ne, min_cost = 1, 0
    a, b, u, v = 0, 0, 0, 0
    print("enter number of vertices")
    n = int(input())
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    cost = [[8, 6, 2], [5, 8, 9], [2, 6, 3]]
    while ne < n:
        mini = 999
        for i in range(n):
            for j in range(n):
                if find(parent, i) != find(parent, j) and cost[i][j] < mini:
                    mini = cost[i][j]
                    a = u = i
                    b = v = j
        
        if find(parent, u) != find(parent, v):
            print("edge ", ne, " from ", a, "->", b, "=", mini)
            ne += 1
            min_cost += mini
            union(parent, rank, u, v)

        cost[a][b] = cost[b][a] = 999
    print("minimum cost =", min_cost)

kruskal()
