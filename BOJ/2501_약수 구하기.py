# 2023-08-24 (08-25)
N, K = map(int, input().split())

k = 1
ans = 0
for _ in range(1, N+1) :
    if N % _ == 0 :
        if k == K : 
            ans = _
            break
        else : k += 1
print(ans)
