# 2023-12-26
m = int(input())
n = int(input())

arr = list(range(2, n+1))
for p in arr :
    for _ in arr :
        if p < _ :
            if _ % p == 0 : arr.remove(_)

ans = [_ for _ in arr if _ >= m and _ <= n]
if not ans : print(-1)
else :
    print(sum(ans))
    print(ans[0])