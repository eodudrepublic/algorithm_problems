# 2023-03-30 (03-31)
import sys
from collections import deque

row = (-1, 1, 0, 0)
col = (0, 0, 1, -1)

def bfs(matrix, x, y) :
    queue = deque()
    queue.append((x, y))
    matrix[x][y] = 0 
    area = 1
    
    while queue : 
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + row[i]
            ny = y + col[i]
            
            if nx < 0 or nx >= X or ny < 0 or ny >= Y :
                continue
                
            if matrix[nx][ny] == 1 :
                area += 1
                queue.append((nx,ny))
                matrix[nx][ny] = 0
    return area

X, Y = map(int, sys.stdin.readline().split())

matrix = []
for l in range(X) :
    line = list(map(int, sys.stdin.readline().split()))
    matrix.append(line)
# print(matrix)

p_n = 0
max_a = 0

for x in range(X) :
    for y in range(Y) :
        if matrix[x][y] == 1 :
            a = bfs(matrix, x, y)
            p_n += 1
            if a > max_a :
                max_a = a

print(p_n)
print(max_a)