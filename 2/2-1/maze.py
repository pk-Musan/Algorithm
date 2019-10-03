# 幅優先探索（BFS） #
"""
    Queueを使うパターンが多い？
    一つの要素に対して一番近いものをすべて見る
"""
import queue

N, M = map(int, input().split())
maze = [[elem for elem in input()] for n in range(N)]
visited = [[-1 for m in range(M)] for n in range(N)]

def move(y, x):
    return [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]

def bfs():
    q = queue.Queue()

    y, x = [(y, x) for y, row in enumerate(maze) for x, elem in enumerate(row) if elem == 'S'][0]

    visited[y][x] = 0

    while(True):
        for next_y, next_x in move(y, x):
            if 0 <= next_y < N and 0 <= next_x < M:
                if maze[next_y][next_x] != '#' and visited[next_y][next_x] == -1:
                    q.put([next_y, next_x])
                    visited[next_y][next_x] = visited[y][x] + 1
        
        y, x = q.get()
        if maze[y][x] == 'G':
            break
    
    print(visited[y][x])
                    
if __name__ == "__main__":
    bfs()