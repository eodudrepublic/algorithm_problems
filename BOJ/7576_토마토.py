# 2023-05-09
import sys
from collections import deque
DAY = 0

X = (-1, 0, 1, 0)
Y = (0, -1, 0, 1)

def bfs(matrix, queue) :
    temp = deque()
    
    while queue : 
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + X[i]
            ny = y + Y[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            
            if matrix[nx][ny] == 0 :
                temp.append((nx,ny))
                matrix[nx][ny] = 1
    
    return temp

def is_ripe(matrix) :
    for l in matrix :
        for t in l :
            if t == 0 :
                return True                
    return False

M, N = map(int, sys.stdin.readline().split())

arr = []
for n in range(N) :
    line = list(map(int, sys.stdin.readline().split()))
    arr.append(line)

if not is_ripe(arr) :
    print(DAY)
    sys.exit()

queue = deque()
for n in range(N) :
    for m in range(M) :
        if arr[n][m] == 1 :
            queue.append((n, m))

while queue :
    DAY += 1
    queue = bfs(arr, queue)

if is_ripe(arr) :
    DAY = 0

print(DAY-1)