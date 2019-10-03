# 通常の実装 #
"""
    fibの処理は指数関数的に広がるので，nが大きいとかなり遅くなる．
    n = 10 の時，fib(9) と fib(8) が呼び出され，
    fib(9)から fib(8) と fib(7) が呼び出される．
    この時点で fib(8) を2回呼び出していることになり，無駄が生じている
"""
N = int(input())

def fib1(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# メモ探索とか動的計画法的な考え方を使う #
memo = [0]*(N+1)
def fib2(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fib2(n-1) + fib2(n-2)
        return memo[n]

print(memo)
print(fib2(N))