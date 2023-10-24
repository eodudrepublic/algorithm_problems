import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num = deque(sys.stdin.readline().rstrip())
returnNum = deque()

while k != 0 and n != k :
    a = num.popleft()
    b = num.popleft()
    # 모르겠다...