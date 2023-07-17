# 2023-05-23
import sys
from collections import deque

INF = 1e9

def bfs(arr, N) :
    queue = deque()
    queue.append(N)
    
    while queue :
        p = queue.popleft()
        if p - 1 >= 0 and arr[p-1] == INF :
            arr[p-1] = arr[p] + 1
            queue.append(p-1)
            if p - 1 == K : return arr[p-1]
        if p + 1 <= 100000 and arr[p+1] == INF :
            arr[p+1] = arr[p] + 1
            queue.append(p+1)
            if p + 1 == K : return arr[p+1]
        if p * 2 <= 100000 and arr[2*p] == INF :
            arr[2*p] = arr[p] + 1
            queue.append(2*p)
            if 2 * p == K : return arr[2*p]

arr = [INF]*100001
N, K = map(int, sys.stdin.readline().split())
if N == K : 
    print(0)
    sys.exit()
arr[N] = 0
print(bfs(arr, N))