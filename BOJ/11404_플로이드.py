# 2023-04-19
import sys

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dp = [[INF] * N for _ in range(N)]

for a in range(N) :
    for b in range(N) :
        if a == b :
            dp[a][b] = 0

for m in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    if  dp[a-1][b-1] > c :
        dp[a-1][b-1] = c
    
for n in range(N) :
    for a in range(N) :
        for b in range(N) :
            dp[a][b] = min(dp[a][b], dp[a][n] + dp[n][b])

for a in dp :
    for b in a :
        if b != INF :
            sys.stdout.write(''.join([str(b), ' ']))
        else :
            sys.stdout.write('0 ')
    sys.stdout.write('\n')