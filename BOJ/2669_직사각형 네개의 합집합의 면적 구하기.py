# 2024-01-26
import sys

arr = [[0 for _ in range(101)] for _ in range(101)]

ans = 0
for _ in range(4) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            if arr[x][y] == 0 :
                arr[x][y] = 1
                ans += 1

sys.stdout.write(''.join([str(ans), '\n']))