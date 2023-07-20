# 2023-07-20
T = int(input())
for t in range(T) :
    arr = list(input().split())
    n = float(arr.pop(0))
    for _ in arr :
        if _ == '@' :
            n *= 3
        elif _ == '%' :
            n += 5
        else :
            n -= 7
    print(f'{n:.2f}')