# 2023-05-02
import sys
from collections import deque

def bfs(arr, n) :
    queue = deque()
    queue.append(n)
    arr[n] = 1
    
    while queue :
        p = queue.popleft()
        
        for t in Tree :
            
            if t[0] == p and arr[t[1]] == 0 :
                queue.append(t[1])
                arr[t[1]] = 1
            
            if t[1] == p and arr[t[0]] == 0 :
                queue.append(t[0])
                arr[t[0]] = 1

CN = int(sys.stdin.readline())
infected = [0]*(CN+1)

TN = int(sys.stdin.readline())
Tree = []
for tn in range(TN) :
    t = list(map(int, sys.stdin.readline().split()))
    Tree.append(t)  

bfs(infected, 1)

num = 0
for i in range(2, CN+1) :
    if infected[i] == 1 :
        num += 1

sys.stdout.write(''.join([str(num), '\n']))