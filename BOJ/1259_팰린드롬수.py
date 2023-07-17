# 2023-05-14 (05-15)
import sys

N = []
while True :
    N = list(sys.stdin.readline().strip())
    if N == ['0'] :
        break
    L = len(N)
    for i in range(L//2) :
        if N[i] != N[L-i-1] :
            L = -1
            break
    if L == -1 :
        sys.stdout.write("no\n")
    else :
        sys.stdout.write("yes\n")