# 2024-02-24
import sys

while True :
    N = int(sys.stdin.readline())
    if N == 0 : break
    
    arr = []
    h = []
    for n in range(N) :
        name, height = sys.stdin.readline().rstrip().split()
        arr.append((float(height), name))
        h.append(float(height))
    
    top = max(h)
    for _ in arr :
        if _[0] == top : sys.stdout.write(''.join([_[1], ' ']))
    sys.stdout.write('\n')