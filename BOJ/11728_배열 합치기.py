# 2024-01-25
a, b = map(int, input().split())
arr1 = input()
arr2 = input()
arr = ' '.join([arr1, arr2])
ans = sorted(map(int, arr.split()))
print(*ans)