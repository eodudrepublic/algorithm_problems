# 2023-06-06 (06-07)
import sys

input = sys.stdin.readline

def fn(m, M) :
    if m == M :
        t = tuple([arr[_] for _ in temp])
        ans.add(t)
        return
    
    for i in range(N) :
        if not visit[i] :
            temp[m] = i
            visit[i] = True
            fn(m+1, M)
            visit[i] = False

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
temp = [0 for _ in range(M)]
visit = [False for _ in range(N)]

ans = set()
fn(0, M)

result = sorted(list(ans))
for _ in result :
    print(*_)