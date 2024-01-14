# 2024-01-14
arr = sorted(map(int, input().split()))

ans = arr[0]
while True :
    ans += 1
    tmp = 0
    if ans % arr[0] == 0 : tmp += 1
    if ans % arr[1] == 0 : tmp += 1
    if ans % arr[2] == 0 : tmp += 1
    if ans % arr[3] == 0 : tmp += 1
    if ans % arr[4] == 0 : tmp += 1
    if tmp >= 3 : break

print(ans)