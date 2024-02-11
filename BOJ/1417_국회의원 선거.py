# 2024-02-11 (02-12)
import sys

def is_max(arr, n) :
    for _ in range(1, n) :
        if arr[_] >= arr[0] : return False
    return True

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
ans = 0
while True :
    if is_max(arr, n) : break
    max_num = max(arr)
    for _ in range(1, n) :
        if arr[_] == max_num :
            arr[_] -= 1
            arr[0] += 1
            ans += 1
        if arr[0] > max_num : break

sys.stdout.write(''.join([str(ans), '\n']))
