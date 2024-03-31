# 2024-03-31 (04-01)
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    arr = {}
    for i in range(4) :
        arr[i] = list(map(int, sys.stdin.readline().split()))
    l = []
    for i in range(3, 0, -1) :
        for j in range(i-1, -1, -1) :
            l.append((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)
    l.sort()
    if l[0] == l[1] == l[2] == l[3] and l[4] == l[5] :
        sys.stdout.write('1\n')
    else :
        sys.stdout.write('0\n')