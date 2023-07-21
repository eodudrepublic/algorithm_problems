# 2023-07-21 (07-22)
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    arr = []
    N = int(sys.stdin.readline())
    for n in range(N) :
        s, l = sys.stdin.readline().split()
        arr.append((s, int(l)))
    arr.sort(key=lambda x: x[1], reverse=True)
    sys.stdout.write(''.join([arr[0][0], '\n']))