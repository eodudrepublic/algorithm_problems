# 2024-02-17
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    N = int(sys.stdin.readline())
    total = 0
    max_n = 0
    winner = 0
    for n in range(N) :
        r = int(sys.stdin.readline())
        total += r
        if r > max_n :
            winner = n + 1
            max_n = r
        elif r == max_n :
            winner = -1
        else : pass
    if winner == -1 : sys.stdout.write('no winner\n')
    else :
        if max_n > total / 2 : sys.stdout.write(''.join(['majority winner ', str(winner), '\n']))
        else : sys.stdout.write(''.join(['minority winner ', str(winner), '\n']))