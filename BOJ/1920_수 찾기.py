# 2023-04-29 (04-30)
import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

for n in X :
    if n in A :
        sys.stdout.write("1\n")
    else :
        sys.stdout.write("0\n")