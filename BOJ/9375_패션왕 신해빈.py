# 2023-06-05
import sys
from itertools import combinations

input = sys.stdin.readline

TC = int(input())
for t in range(TC) :
    N = int(input())
    if N == 0 : 
        print(0)
        continue
    
    closet = {}
    key = []
    for n in range(N) :
        c, tag = input().split()
        if tag not in key :
            key.append(tag)
            closet[tag] = 1
        else :
            closet[tag] += 1

    ans = 1
    # 각 종류 옷의 개수 + 1(안 입는 경우)를 모두 곱해준 수에 1(모든 옷을 안 입는 경우)만 빼주면 쉽게 계산할 수 있었음
    for k in key :
        ans *= closet[k] + 1
    print(ans-1)