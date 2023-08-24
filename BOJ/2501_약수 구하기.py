# 2023-08-24 solve
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
