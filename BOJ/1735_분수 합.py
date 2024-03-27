# 2024-03-27 (03-28)
import sys

def GCD(x, y) :
    while y :
        x, y = y, x % y
    return x

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
ans1 = a * d + b * c
ans2 = b * d
gcd = GCD(ans1, ans2)
sys.stdout.write(''.join([str(ans1//gcd), ' ', str(ans2//gcd), '\n']))