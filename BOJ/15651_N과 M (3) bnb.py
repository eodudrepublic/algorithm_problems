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
        ans[m] = i + 1
        fn(m+1, M)
    
N, M = map(int, input().split())
ans = [0 for _ in range(M)]
fn(0, M)