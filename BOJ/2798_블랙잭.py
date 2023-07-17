# 2023-05-26
import sys

N, M = map(int, sys.stdin.readline().split())
deck = list(map(int, sys.stdin.readline().split()))

sum = []
for i in range(0, N) :
    for j in range(i+1, N) :
        for l in range(j+1, N) :
            temp = deck[i] + deck[j] + deck[l]
            if temp == M :
                print(temp)
                sys.exit()
            if temp < M :
                sum.append(temp)
sum.sort()
print(sum[-1])