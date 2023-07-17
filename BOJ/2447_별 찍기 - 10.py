# 2023-04-09
import sys

star = [
    ['*', '*', '*'],
    ['*', ' ', '*'],
    ['*', '*', '*']
]

def expand(N, star) :
    new_star = []
    for n in range(N) :
        tmp = int(N/3)
        if n < N/3 :
            new_star.append(star[n]*3)
        elif n < 2*N/3 :
            new_star.append(star[n%tmp]+[' ']*tmp+star[n%tmp])
        else :
            new_star.append(star[n%tmp]*3)
    return new_star

N = int(sys.stdin.readline())
n = 3
while n != N :
    n = n*3
    star = expand(n, star)
for l in star :
    for s in l :
        print(s, end='')
    print()