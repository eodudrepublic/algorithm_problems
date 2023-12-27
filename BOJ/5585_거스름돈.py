# 2023-12-27
money = 1000 - int(input())
arr = (500, 100, 50, 10, 5, 1)

ans = 0
for _ in arr :
    ans += money // _
    money %= _
    if money == 0 : break

print(ans)