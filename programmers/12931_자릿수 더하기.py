# 2024-03-13
import sys

def solution(n):
    answer = 0

    line = str(n)
    for _ in line :
        answer += int(_)

    return answer

def main() :
    n = int(sys.stdin.readline())
    sys.stdout.write(''.join([str(solution(n)), '\n']))

if __name__ == "__main__" :
    main()