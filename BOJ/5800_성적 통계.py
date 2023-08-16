# 2023-08-16 (08-17)
T = int(input())
for t in range(1, T+1) :
    arr = list(map(int, input().split()))
    n =  arr.pop(0)
    arr.sort()
    gap = 0
    for _ in range(1, n) :
        if arr[_] - arr[_-1] > gap : gap = arr[_] - arr[_-1]
    print('Class', t)
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {gap}')