# 2023-06-15
import sys
from queue import PriorityQueue

INF = 1e9
input = sys.stdin.readline
print = sys.stdout.write

def bnb(pw, pv, rv, n) :
    if ANS[0] > pv + rv : return
    if pw > K : return
    
    if pv > ANS[0] : ANS[0] = pv
    
    if n == N : return
    
    bnb(pw + items[n][2], pv + items[n][1], items[n+1][0]*(pw+items[n][2]-K), n+1)
    bnb(pw, pv, items[n+1][0]*(pw-K), n+1)

K, N = map(int, input().split())

temp = PriorityQueue()
total_w = 0
total_v = 0
for n in range(N) :
    W, V = map(int, input().split())
    total_w += W
    total_v += V
    temp.put((-1*V/W, V, W))

if total_w <= K :
    print(''.join([str(total_v), '\n']))
    sys.exit(0)

items = {N:(0, 0)}
for n in range(N) : items[n] = temp.get()

ANS = [0]
bnb(0, 0, INF, 0)
print(''.join([str(ANS[0]), '\n']))