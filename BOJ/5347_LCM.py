# 2024-02-03 (02-04)
T = int(input())
for t in range(T) :
    n, m = map(int, input().split())
    temp = min(n, m)
    i = 1
    while True :
        ans = temp * i
        if ans % n == 0 and ans % m == 0 : break
        i += 1
    print(temp * i)
