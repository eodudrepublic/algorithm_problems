# 2023-05-04
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    n, k, tn, M = map(int, sys.stdin.readline().split())
    TS = [[0]*(n+1)]
    for i in range(n) : TS.append([0]*(k+1))
    for m in range(M) :
        id, q, s = map(int, sys.stdin.readline().split())
        TS[0][id] += 1
        TS[id][0] = m
        if TS[id][q] < s :
            TS[id][q] = s
    
    TR = []
    for i in range(1, n+1) : TR.append([sum(TS[i][1:]), M-TS[0][i], M-TS[i][0], i])
    TR.sort(reverse=True)
    
    for i in range(n) :
        if TR[i][-1] == tn :
            print(i+1)
            break