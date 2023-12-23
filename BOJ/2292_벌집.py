# 2023-12-23
n = int(input())
N = 1
tmp = 0
while True : 
    if n <= N : 
        print(tmp + 1)
        break
    else : 
        tmp += 1
        N += 6 * tmp