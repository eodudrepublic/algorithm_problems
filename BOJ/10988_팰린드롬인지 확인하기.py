# 2023-07-27 (07-28)
arr = list(input())
_arr = arr[::-1]

L = len(arr)
T = 1
for _ in range(L) :
    if arr[_] == _arr[_] : pass
    else : 
        T = 0
        break
print(T)