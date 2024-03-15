# 2024-03-15
N, K = map(int, input().split())
arr = [_ for _ in range(2, N+1)]
k = 0
ans = 0
while k != K :
    ans = temp = arr.pop(0)
    k += 1
    i = 1
    while temp * i <= N :
        if k == K :
            break
        i += 1
        if temp * i in arr :
            arr.remove(temp*i)
            ans = temp * i
            k += 1
print(ans)