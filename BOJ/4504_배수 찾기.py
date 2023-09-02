# 2023-09-02
n = int(input())
while True :
    _ = int(input())
    if _ == 0 : break
    if _ % n == 0 : print(f'{_} is a multiple of {n}.')
    else : print(f'{_} is NOT a multiple of {n}.')