# 2024-01-13
n = int(input())
arr = list(map(int, input().split()))

start, end = arr[0], arr[0]
ans = 0
for i in range(1, n) :
    if arr[i] > end : 
        end = arr[i]
    else : 
        if end - start > ans : ans = end - start
        start = arr[i]
        end = arr[i]
if end - start > ans : ans = end - start
print(ans)