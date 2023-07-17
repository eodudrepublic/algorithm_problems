# 2023-06-16 (06-17)
import sys
from queue import PriorityQueue

INF = 1e9
input = sys.stdin.readline
print = sys.stdout.write

def bnb(pw, pv, rv, n) :
    if ANS[0] > pv + rv : return
    if pw >= 100 : return
    
    if pv > ANS[0] : ANS[0] = pv
    
    if n == N : return
    
    bnb(pw + items[n][2], pv + items[n][1], items[n+1][0]*(pw+items[n][2]-100), n+1)
    bnb(pw, pv, items[n+1][0]*(pw-100), n+1)

N = int(input())

s = list(map(int, input().split()))
h = list(map(int, input().split()))
temp = []
for _ in range(N) :
    if s[_] == 0 :
        temp.append((-1*INF, h[_], 0))
    elif h[_] == 0 :
        temp.append((0, 0, s[_]))
    else :
        temp.append((-1*h[_]/s[_], h[_], s[_]))
temp.sort()

items = {N:(0, 0)}
for n in range(N) : items[n] = temp[n]

ANS = [0]
bnb(0, 0, INF, 0)
print(''.join([str(ANS[0]), '\n']))