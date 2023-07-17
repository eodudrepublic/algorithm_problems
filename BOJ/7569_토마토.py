# 2023-05-09
import sys
from collections import deque
DAY = 0

X = (-1, 0, 0, 1, 0, 0)
Y = (0, -1, 0, 0, 1, 0)
Z = (0, 0, -1, 0, 0, 1)

def bfs(matrix, queue) :
    temp = deque()
    
    while queue : 
        x, y, z = queue.popleft()
        
        for i in range(6) :
            nx = x + X[i]
            ny = y + Y[i]
            nz = z + Z[i]
            
            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M :
                continue
            
            if matrix[nx][ny][nz] == 0 :
                temp.append((nx,ny,nz))
                matrix[nx][ny][nz] = 1
    
    return temp

def is_ripe(matrix) :
    for m in matrix :
        for l in m :
            for t in l :
                if t == 0 :
                    return True
    return False

M, N, H = map(int, sys.stdin.readline().split())

arr = []
for h in range(H) :
    matrix = []
    for n in range(N) :
        line = list(map(int, sys.stdin.readline().split()))
        matrix.append(line)
    arr.append(matrix)

if not is_ripe(arr) :
    print(DAY)
    sys.exit()

queue = deque()
for h in range(H) :
    for n in range(N) :
        for m in range(M) :
            if arr[h][n][m] == 1 :
                queue.append((h, n, m))

while queue :
    DAY += 1
    queue = bfs(arr, queue)

if is_ripe(arr) :
    DAY = 0

print(DAY-1)