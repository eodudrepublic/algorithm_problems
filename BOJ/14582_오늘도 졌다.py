# 2024-02-09
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
score1 = 0
score2 = 0
ans = False
for _ in range(9) :
    if arr1[_] == 0 and arr2[_] == 0 : continue
    if score1 + arr1[_] > score2 : ans = True
    score1 += arr1[_]
    score2 += arr2[_]

if ans : print('Yes')
else : print('No')
