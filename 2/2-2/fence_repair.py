N = int(input())
L = list(map(int, input().split()))

ans = 0
L = sorted(L)
i = 0
while i < N-1:
    t = L[i] + L[i+1]
    ans += t
    L[i+1] = t
    i +=1
    
print(ans)