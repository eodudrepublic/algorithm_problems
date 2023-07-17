# 2023-04-03 (04-04)
import sys

N = int(sys.stdin.readline())
sList = []
for n in range(N) :
    book = sys.stdin.readline().strip()
    sList.append(book)
sList.sort()

maxBook = ""
exBook = ""
m = 0
n = 0
for b in sList :
    if b != exBook :
        if n > m :
            maxBook = exBook
            m = n
        exBook = b
        n = 1
    else :
        n += 1
if n > m :
    maxBook = exBook

print(maxBook)