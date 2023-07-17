# 2023-05-20 (05-21)
import sys

N = int(sys.stdin.readline())

for n in range(N) :
    arr = list(map(int, sys.stdin.readline().split()))
    total = arr[0]
    avg = sum(arr[1:])/total
    num = 0
    for i in range(1, total+1) :
        if arr[i] > avg :
            num += 1
    sys.stdout.write("{:.3f}%\n".format(100*num/total, 3))