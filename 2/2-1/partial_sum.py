N = int(input())
A = list(map(int, input().split()))
# A = [int(a) for a in input().split()]
partial_sum = int(input())

def dfs(i, sum_value):
    print("i: {0}, sum: {1}".format(i, sum_value))
    if i == N:
        return sum_value == partial_sum
    if dfs(i+1, sum_value):
        return True
    if dfs(i+1, sum_value + A[i]):
        return True
    
    return False
    
if dfs(0, 0):
    print("Yes")
else:
    print("No")