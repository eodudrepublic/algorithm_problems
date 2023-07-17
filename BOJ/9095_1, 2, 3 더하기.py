# 2023-05-24
import sys
from collections import deque

def bfs(arr, sp) :
    queue = deque()
    queue.append(sp)
    
    while queue :
        n = queue.popleft()
        
        if n + 1 <= 11 :
            arr[n+1] += 1
            queue.append(n+1)
        else : continue
        if n + 2 <= 11 :
            arr[n+2] += 1
            queue.append(n+2)
        else : continue
        if n + 3 <= 11 :
            arr[n+3] += 1
            queue.append(n+3)

arr = [0 for _ in range(12)]
bfs(arr, 0)

T = int(sys.stdin.readline())
for t in range(T) :
    n = int(sys.stdin.readline())
    print(arr[n])