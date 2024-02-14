# 2024-02-14
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    ans = 0
    temp = list(map(int, sys.stdin.readline().split()))
    arr = [temp[1]]
    for _ in range(2, 21) :
        arr.append(temp[_])
        i = _ - 1
        while True :
            if i == 0 or (arr[i - 1] < arr[i]): break
            else :
                ans += 1
                tmp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = tmp
                i -= 1
    sys.stdout.write(''.join([str(temp[0]), ' ', str(ans), '\n']))