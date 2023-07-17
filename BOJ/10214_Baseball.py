# 2023-07-17
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    game = {'Yonsei' : 0, 'Korea' : 0}
    for _ in range(9) :
        y, k = map(int, sys.stdin.readline().split())
        game['Yonsei'] += y
        game['Korea'] += k
    if game['Yonsei'] > game['Korea'] : sys.stdout.write('Yonsei\n')
    elif game['Yonsei'] < game['Korea'] : sys.stdout.write('Korea\n')
    else : sys.stdout.write('Draw\n')