# 2023-12-17 (12-18)
arr = []
for _ in range(5) :
    a = int(input())
    arr.append(a)
arr.sort()
print(int(sum(arr)/len(arr)))
print(arr[2])
