# 2024-03-25
N = int(input())
a = N // 5
b = N % 5
ans = 0
while True :
    if b % 3 == 0 :
        ans = a + b // 3
        break
    else :
        a -= 1
        b += 5
        if a < 0 : break
if ans == 0 :
    print(-1)
else :
    print(ans)