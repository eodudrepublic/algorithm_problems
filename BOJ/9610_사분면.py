# 2023-07-03
import sys

N = int(sys.stdin.readline())
arr = [0, 0, 0, 0, 0]
for n in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0 : arr[0] += 1
    elif x > 0 and y > 0 : arr[1] += 1
    elif x < 0 and y > 0 : arr[2] += 1
    elif x < 0 and y < 0 : arr[3] += 1
    else : arr[4] += 1
for _ in range(1, 5) :sys.stdout.write(''.join(['Q', str(_), ': ', str(arr[_]), '\n']))
sys.stdout.write(''.join(['AXIS: ', str(arr[0]), '\n']))