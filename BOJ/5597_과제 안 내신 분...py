# 2023-08-28
arr = list(range(1, 31))
for _ in range(28) :
    n = int(input())
    arr.remove(n)
for _ in arr : print(_)