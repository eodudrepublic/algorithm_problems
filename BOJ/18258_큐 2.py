# 2023-10-21 (10-22)
from collections import deque
import sys

def print(_) :
    sys.stdout.write(str(_))
    sys.stdout.write('\n')

q = deque()
N = int(sys.stdin.readline())
for n in range(N) :
    op = sys.stdin.readline().rstrip()
    try : 
        push, n = op.split()
        q.append(int(n))
    except : 
        if op == 'front' : 
            if q : print(q[0])
            else : print(-1)
        elif op == 'back' :
            if q : print(q[-1])
            else : print(-1)
        elif op == 'size' :
            print(len(q))
        elif op == 'empty' :
            if q : print(0)
            else : print(1)
        else : 
            if q : print(q.popleft())
            else : print(-1)
    