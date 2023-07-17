# 2023-06-05
import sys

input = sys.stdin.readline
print = sys.stdout.write

def fn(n, M) :
    if n == M :
        print(' '.join(str(_) for _ in ans))
        print('\n')
        return
    
    for i in range(N) :
        if not visit[i] :
            ans[n] = i + 1
            for _ in range(i+1) : visit[_] = True
            fn(n+1, M)
            for _ in range(i+1) : visit[_] = False

N, M = map(int, input().split())
ans = [0 for _ in range(M)]
visit = [False for _ in range(N)]
fn(0, M)