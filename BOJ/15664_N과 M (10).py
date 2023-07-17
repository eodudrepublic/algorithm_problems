# 2023-06-08 (06-09)
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
            for _ in range(i+1) : visit[_] = True
            fn(m+1, M)
            for _ in range(i+1) : visit[_] = False

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
temp = [0 for _ in range(M)]
visit = [False for _ in range(N)]

ans = set()
fn(0, M)

result = sorted(list(ans))
for _ in result :
    print(*_)