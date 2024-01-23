# 2024-01-23
import sys

arr = [[0 for _ in range(100)] for _ in range(100)]

N = int(sys.stdin.readline())
ans = 0
for n in range(N) :
    X, Y = map(int, sys.stdin.readline().split())
    for x in range(X - 1, X + 9) :
        for y in range(Y - 1, Y + 9) : 
            if arr[x][y] == 0 : 
                arr[x][y] = 1
                ans += 1

sys.stdout.write(''.join([str(ans), '\n']))