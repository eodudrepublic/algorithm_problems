# 2023-12-28
r = 31
M = 1234567891
L = int(input())
line = input()

hash = 0
for l in range(L) :
    hash += ((ord(line[l]) - 96) * (31**l)) % M
print(hash % M)