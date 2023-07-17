# 2023-06-11
import sys

input = sys.stdin.readline
print = sys.stdout.write

def fn(n, N) :
    if n == N :
        ANS[0] += 1
        return
    
    for i in range(N) :
        if not col[i] and not up[n+i] and not down[n-i+N-1]:
            col[i] = up[n+i] = down[n-i+N-1] = True
            fn(n+1, N)
            col[i] = up[n+i] = down[n-i+N-1] = False

N = int(input())
col = [False for _ in range(N)]
up = [False for _ in range(2*N-1)]
down = [False for _ in range(2*N-1)]
ANS = [0, '\n']

fn(0, N)
print(''.join([str(_) for _ in ANS]))