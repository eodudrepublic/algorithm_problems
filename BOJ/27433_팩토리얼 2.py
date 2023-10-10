# 2023-10-11
N = int(input())
total = 1
while True :
    if N == 0 : 
        print(1)
        break
    if N == 1 :
        print(total)
        break
    total *= N
    N -= 1