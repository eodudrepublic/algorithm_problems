# 2024-04-04
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dic = {n+1:arr[n] for n in range(N)}
    arr.sort()
    ans = 0
    while arr : 
        start = arr.pop(0)
        end = dic[start]
        while start != end :
            arr.remove(end)
            end = dic[end]
        ans += 1
    sys.stdout.write(''.join([str(ans), '\n']))