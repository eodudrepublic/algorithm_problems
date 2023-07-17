# 2023-05-25
import sys
from collections import deque

def bfs(tree, visited, sp) :
    queue = deque()
    queue.append(sp)
    visited[sp] = 1
    
    while queue :
        p = queue.popleft()
        
        for i in tree[p] :
            if visited[i] == 1 : continue
            queue.append(i)
            visited[i] = 1

def findConnected(tree, visited, N) :
    cc = 0
    for n in range(1, N+1) :
        if visited[n] == 0 :
            cc += 1
            bfs(tree, visited, n)
    return cc

N, M = map(int, sys.stdin.readline().split())
visited = [1]
visited.extend([0 for _ in range(N)])
tree = [[0]]
tree.extend([[] for _ in range(N)])
for m in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

print(findConnected(tree, visited, N))