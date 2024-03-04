import sys

matrix = [[1, 1], [1, 0]]
m = [[1, 1], [1, 0]]

def mul_matrix() :
    temp = [[0, 0], [0, 0]]
    for x in range(2) :
        for y in range(2) :
            for z in range(2) :
                temp[x][y] += matrix[x][z] * m[z][y]
    return temp

for _ in range(8) :
    matrix = mul_matrix()
print(matrix)