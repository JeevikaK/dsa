def knapsack(W, wt, val, n):
    K = [[0 for i in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(val[i-1] + K[i-1][j-wt[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    return K[n][W]

val = [2, 3, 1, 6, 7]
wt = [1, 5, 2, 4, 3]
W = 20
n = len(val)
print(knapsack(W, wt, val, n))