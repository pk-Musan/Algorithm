N, R = map(int, input().split())
X = list(map(int, input().split()))

i = 0
ans = 0
X = sorted(X)

while i < N-1:
    left_X = X[i]
    i +=1
    
    while i < N and X[i] <= left_X + R:
        i +=1
        
    ans +=1
    
print(ans)