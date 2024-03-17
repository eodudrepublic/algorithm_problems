# 2024-03-17 (03-18)
N = int(input())
ans = 0
while N > 0 :
    if N == 100000000 :
        ans += 9
        N = 99999999
    elif N // 10000000 != 0 :
        temp = N - 9999999
        ans += 8 * temp
        N = 9999999
    elif N // 1000000 != 0 :
        temp = N - 999999
        ans += 7 * temp
        N = 999999
    elif N // 100000 != 0 :
        temp = N - 99999
        ans += 6 * temp
        N = 99999
    elif N // 10000 != 0 :
        temp = N - 9999
        ans += 5 * temp
        N = 9999
    elif N // 1000 != 0 :
        temp = N - 999
        ans += 4 * temp
        N = 999
    elif N // 100 != 0 :
        temp = N - 99
        ans += 3 * temp
        N = 99
    elif N // 10 != 0 :
        temp = N - 9
        ans += 2 * temp
        N = 9
    else :
        ans += N
        N = 0
print(ans)