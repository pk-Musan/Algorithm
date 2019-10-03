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

print(knapsack(0, w_max))


# DPを使った手法 #