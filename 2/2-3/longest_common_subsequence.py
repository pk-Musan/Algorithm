n = int(input('n = '))
m = int(input('m = '))
s = list(input('s: '))
t = list(input('t: '))

# DP使う
# dp[i][j]: s1...siとt1...tjに対する最長共通部分列の長さ

dp = [ [0 for j in range(m+1)] for i in range(n+1) ]
print(s)

def solve():
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    return dp[n][m]

print(solve())