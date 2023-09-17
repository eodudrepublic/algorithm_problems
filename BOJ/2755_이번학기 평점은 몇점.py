# 2023-09-17 (09-18)
import sys

score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
total = 0
div = 0
N = int(sys.stdin.readline())
for n in range(N) :
    a, b, c = sys.stdin.readline().split()
    total += int(b) * score[c]
    div += int(b)
print("%.2f" % (round(total/div + 10**-10, 2)))
# 엄... 사사오입 ㅈ까고 이거나 쓰자...