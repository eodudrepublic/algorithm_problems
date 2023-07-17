# 2023-06-06
import sys

input = sys.stdin.readline
print = sys.stdout.write

def fn(m, M) :
    if m == M :
        print(' '.join([str(_) for _ in ans]))
        print('\n')
        return
    
    for i in range(N) :
        if not visit[i] :
            ans[m] = i + 1
            for _ in range(i) : visit[_] = True
            fn(m+1, M)
            for _ in range(i) : visit[_] = False

N, M = map(int, input().split())
ans = [0 for _ in range(M)]
visit = [False for _ in range(N)]
fn(0, M)