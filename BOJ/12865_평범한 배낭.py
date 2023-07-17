import sys

input = sys.stdin.readline
print = sys.stdout.write

def bnb(pw, pv, n) :
    tmp = items[n]
    if ANS[0] >= pv + tmp[0]*(pw-K) : return
    if pw > K : return
    
    if pv > ANS[0] : ANS[0] = pv
    
    if n == N : return
    
    bnb(pw + tmp[2], pv + tmp[1], n+1)
    bnb(pw, pv, n+1)

N, K = map(int, input().split())

temp = []
for n in range(N) :
    W, V = map(int, input().split())
    if V == 0 : N -= 1
    else : temp.append((-1*V/W, V, W))

temp.sort()
items = {N:(0, 0)}
for n in range(N) : items[n] = temp[n]

ANS = [0]
bnb(0, 0, 0)
print(''.join([str(ANS[0]), '\n']))