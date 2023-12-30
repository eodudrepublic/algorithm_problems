# 2023-12-30
n, k = map(int, input().split())
arr = sorted(map(int, input().split()), reverse=True)
print(arr[k-1])