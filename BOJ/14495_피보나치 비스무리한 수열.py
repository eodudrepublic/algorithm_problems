# 2024-03-21
arr = {0:1, 1:1, 2:1}
N = int(input())
for n in range(3, N) :
    arr[n] = arr[n-3] + arr[n-1]
print(arr[N-1])
