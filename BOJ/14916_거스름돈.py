# 2024-01-15
n = int(input())

ans = 0
while True :
    if n % 5 == 0 : 
        ans += (n // 5)
        break
    ans += 1
    n -= 2
    if n == 0 : break
    if n < 0 :
        ans = -1
        break
print(ans)
