# 2023-05-08 (05-09)
import sys
from collections import deque
DFS = []
BFS = []

def dfs(tree, v) :
    DFS.append(v)
    
    for node in tree[v] :
        if node not in DFS :
            dfs(tree, node)

def bfs(tree, v) :
    queue = deque()
    queue.append(v)

    BFS.append(v)
    
    while queue :
        v = queue.popleft()
        for i in tree[v] :
            if i not in BFS :
                BFS.append(i)
                queue.append(i)
                
N, M, V = map(int, sys.stdin.readline().split())

tree = {}
for n in range(1, N+1) :
    tree[n] = []
    
for m in range(M) :
    v1, v2 = map(int, sys.stdin.readline().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

for n in range(1, N+1) :
    tree[n].sort()

dfs(tree, V)
for i in DFS :
    sys.stdout.write(''.join([str(i), ' ']))
sys.stdout.write('\n')

bfs(tree, V)
for i in BFS :
    sys.stdout.write(''.join([str(i), ' ']))
sys.stdout.write('\n')