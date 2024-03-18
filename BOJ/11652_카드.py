# 2024-03-18 (03-19)
import sys

arr = {}
N = int(sys.stdin.readline())
for n in range(N) :
    key = sys.stdin.readline()
    if key in arr :
        arr[key] += 1
    else :
        arr[key] = 1
keys = arr.keys()
ans = ''
num = 0
for _ in keys :
    if arr[_] > num :
        ans = _
        num = arr[_]
    elif arr[_] == num :
        if int(_) < int(ans) :
            ans = _
    else :
        pass
sys.stdout.write(ans)