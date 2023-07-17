# 2023-04-01
import sys
from collections import deque

row = (-2, -2, 2, 2, -1, -1, 1, 1)  # 줄 (가로)
col = (-1, 1, -1, 1, -2, 2, -2, 2)  # 열 (세로)

def bfs(matrix, x, y) :
    queue = deque()
    queue.append((x, y))

    matrix[x][y] = 0 
    
    while queue :
        x, y = queue.popleft()
        
        for i in range(8) :
            nx = x + col[i]
            ny = y + row[i]
            
            if nx < 0 or nx >= L or ny < 0 or ny >= L :
                continue
            
            if matrix[nx][ny] == -1 :
                queue.append((nx,ny))
                matrix[nx][ny] = matrix[x][y] + 1

T = int(sys.stdin.readline())
for t in range(T) :
    L = int(sys.stdin.readline())
    cb = [[-1 for r in range(L)] for c in range(L)]
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    bfs(cb, sx, sy)
    print(cb[ex][ey])