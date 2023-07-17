# 2023-06-11
import sys

input = sys.stdin.readline
print = sys.stdout.write

def fn(m, M) :
    if m == M :
        t = tuple([arr[_] for _ in temp])
        ans.add(t)
        return
    
    for i in range(N) :
        temp[m] = i
        fn(m+1, M)

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
temp = [0 for _ in range(M)]

ans = set()
fn(0, M)

result = sorted(list(ans))
for _ in result :
    print(' '.join([str(i) for i in _]))
    print('\n')