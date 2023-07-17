# 2023-05-13
import sys
from collections import deque

N = int(sys.stdin.readline())

ngw = 0
for n in range(N) :
    word = list(sys.stdin.readline().strip())
    
    p = word[0]
    q = deque([p])
    for w in word :
        if w == p :
            continue
        p = w
        if w in q :
            ngw += 1
            break
        q.append(w)

print(N-ngw)