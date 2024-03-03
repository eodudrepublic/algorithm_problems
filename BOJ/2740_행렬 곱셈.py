# 2024-03-03
import sys

M, X = map(int, sys.stdin.readline().split())
matrix1 = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
X, N = map(int, sys.stdin.readline().split())
matrix2 = [list(map(int, sys.stdin.readline().split())) for _ in range(X)]

ans_matrix = [[0 for n in range(N)] for m in range(M)]
for m in range(M) :
    for n in range(N) :
        for x in range(X) :
            ans_matrix[m][n] += matrix1[m][x] * matrix2[x][n]

for line in ans_matrix :
    for _ in line :
        sys.stdout.write(''.join([str(_), ' ']))
    sys.stdout.write('\n')
    