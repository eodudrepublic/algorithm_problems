# 2023-05-07 (05-08)
import sys

nums = []
numf = [0]*8001
N = int(sys.stdin.readline())

sum = 0
for n in range(N) :
    num = int(sys.stdin.readline())
    sum += num
    nums.append(num)
    numf[num+4000] += 1

print(round(sum/N))

nums.sort()
print(nums[N//2])

m = 0
f = max(numf)
mf = 0
for i in range(8001) :
    if numf[i] == f :
        mf = i - 4000
        m += 1
        if m == 2 :
            break
print(mf)

print(max(nums)-min(nums))