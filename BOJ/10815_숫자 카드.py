# 2023-06-13 (06-14) -> 딕셔너리가 이렇게 빠를 줄 몰랐음
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
temp = map(int, input().split())
deck = {}
for _ in temp : deck[_] = 0

M = int(input())
arr = map(int, input().split())
for _ in arr :
    if _ not in deck :
        print('0 ')
    else :
        print('1 ')
print('\n')