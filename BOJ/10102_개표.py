# 2023-07-15 (07-16)
import sys

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
if arr.count('A') > arr.count('B') : print('A')
elif arr.count('A') == arr.count('B') : print('Tie')
else : print('B')