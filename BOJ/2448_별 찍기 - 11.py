# 2023-04-10
import sys

star = [
    '  *  ',
    ' * * ',
    '*****'
]

def expand(star, n) :
    new_star = []
    for i in range(n) :
        new_star.append(''.join([' '*n, star[i], ' '*n]))
    for i in range(n) :
        new_star.append(''.join([star[i], ' ', star[i]]))
    return new_star

N = int(sys.stdin.readline())
n = 3
while n != N :
    star = expand(star, n)
    n = n * 2

for line in star :
    sys.stdout.write(line)
    print()