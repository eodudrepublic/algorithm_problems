# 2024-01-16
import sys
from itertools import combinations

N = int(sys.stdin.readline())

arr = []
for _ in range(N) : arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(0, N) :
    for j in range(i+1, N) : 
        arr[i][j] += arr[j][i]
        arr[j][i] = 0

team = list(combinations(list(range(N)), N//2))
team_num = len(team)

def calc_stat(a_team, b_team) :
    a_stat = 0
    for i in range(N//2) :
        for j in range(i+1, N//2) : a_stat += arr[a_team[i]][a_team[j]]
    b_stat = 0
    for i in range(N//2) :
        for j in range(i+1, N//2) : b_stat += arr[b_team[i]][b_team[j]]
    return abs(a_stat - b_stat)

ans = calc_stat(team[0], team[team_num - 1])
for _ in range(1, team_num//2) :
    if ans == 0 : break
    temp = calc_stat(team[_], team[team_num - 1 - _])
    if temp < ans : ans = temp

sys.stdout.write(''.join([str(ans), '\n']))