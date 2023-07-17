import itertools
import sys

def tsp_bruteforce(matrix):
    # 도시의 수
    n = len(matrix)

    # 가능한 모든 경로 생성 -> 1~4 순열
    path = list(itertools.permutations(range(1, n)))

    # 최단 경로 초기값 설정
    min_distance = float('inf')
    min_path = None

    # 모든 경로에 대해 거리 계산
    for p in path:
        distance = matrix[0][p[0]]
        for i in range(n-2):
            distance += matrix[p[i]][p[i+1]]
        distance += matrix[p[-1]][0]

        # 현재 경로가 최단 경로보다 짧을 경우, 최단 경로 갱신
        if distance < min_distance:
            min_distance = distance
            min_path = [0] + list(p) + [0]

    return min_path, min_distance

# 그래프 인접 행렬
W = [
    [0, 8, 13, 18, 20], 
    [3, 0, 7, 8, 10], 
    [4, 11, 0, 10, 7], 
    [6, 6, 7, 0, 11], 
    [10, 6, 2, 1, 0]
]

# 최단 경로 계산
min_path, min_distance = tsp_bruteforce(W)

# 결과 출력
print("최단 경로:", min_path)
print("최단 거리:", min_distance)

