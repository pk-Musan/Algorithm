N = int(input("N: "))
w = list(map(int, input("W: ").split()))
v = list(map(int, input("V: ").split()))
w_max = int(input("w_max: "))
dp = [[-1 for w in range(w_max+1)] for n in range(N+1)]

# メモ化を使った手法 #
def knapsack(i, rest_w):
    if dp[i][rest_w] >= 0:
        return dp[i][rest_w]
    
    if i == N:
        res = 0
    elif rest_w < w[i]:
        res = knapsack(i+1, rest_w)
    else:
        res = max( knapsack(i+1, rest_w-w[i]) + v[i], knapsack(i+1, rest_w) )
    
    dp[i][rest_w] = res
    
    return dp[i][rest_w]

# print(knapsack(0, w_max))


# DP(動的計画法)を使った手法 #
dp = [ [0 for w in range(w_max+1)] for n in range(N+1) ]
def solve():
    for i in range(N):
        for j in range(w_max+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max( dp[i][j], dp[i][j-w[i]] + v[i] )

    return dp[N][w_max]

print(solve())