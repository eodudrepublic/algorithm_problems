#2023-04-28 (04-29)
import sys

K = int(sys.stdin.readline())

memo = [0]
for k in range(K) :
    n = int(sys.stdin.readline())
    if n == 0 :
        memo.pop()
    else :
        memo.append(n)

print(sum(memo))