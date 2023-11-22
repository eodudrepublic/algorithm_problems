# 2023-11-22 (11-23)
for _ in range(3) :
    arr = list(input().split())
    if arr.count('0') == 0 : print('E')
    elif arr.count('0') == 1 : print('A')
    elif arr.count('0') == 2 : print('B')
    elif arr.count('0') == 3 : print('C')
    else : print('D')