# 2024-01-30
def pn(n, k) :
    if k == 0 : return 1
    up = 1
    for _ in range(k-1) :
        up *= n - 1 -_
    down = 1
    for _ in range(1, k) :
        down *= _
    return up // down

n, k = map(int, input().split())
print(pn(n, k))