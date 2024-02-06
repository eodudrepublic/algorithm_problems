# 2024-02-06
n, d = map(int, input().split())
temp = ''.join([str(_) for _ in range(1, n+1)])
print(temp.count(str(d)))