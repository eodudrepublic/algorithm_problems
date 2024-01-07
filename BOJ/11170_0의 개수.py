# 2024-01-07 (01-08)
arr = []
for _ in range(0, 1000001) :
    tmp = str(_)
    arr.append(tmp.count('0'))
T = int(input())
for t in range(T) :
    n, m = map(int, input().split())
    ans = 0
    for _ in range(n, m+1) : ans += arr[_]
    print(ans)