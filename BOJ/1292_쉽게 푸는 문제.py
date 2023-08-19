# 2023-08-19
i = 1
_i = 0
arr = []
for _ in range(1000) :
    if i == _i : 
        i += 1
        _i = 0
    arr.append(i)
    _i += 1

x, y = map(int, input().split())
N = 0
for _ in range(x-1, y) : N += arr[_]
print(N)