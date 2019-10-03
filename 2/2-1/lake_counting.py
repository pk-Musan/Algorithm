# 深さ優先探索（DFS） #
"""
    stackを使うケースが多い
    一つの要素に対して掘り下げきる
    １．一番近い場所を取り出す
    ２．取り出した場所から次に近い場所を全てstackに入れる
    ３．１．に戻る
"""
N, M = map(int, input().split())

W = [[w_y for w_y in input()] for n in range(N)]

def move(y, x):
    return [[y-1, x-1], [y-1, x], [y-1, x+1], [y, x-1],
            [y, x+1], [y+1, x-1], [y+1, x], [y+1, x+1]]

def dfs(y, x):
    W[y][x] = '.'
    
    for next_y, next_x in move(y, x):
        if 0 <= next_y < N and 0 <= next_x < M:
            if W[next_y][next_x] == 'W':
                dfs(next_y, next_x)

if __name__ == "__main__":
    puddle = 0
    
    for y in range(N):
        for x in range(M):
            if W[y][x] == 'W':
                dfs(y, x)
                puddle +=1
    
    print(puddle)