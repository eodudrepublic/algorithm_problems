# 2024-03-19
import sys

def solution(n):
    answer = 0
    for _ in range(2, n) :
        if n % _ == 1 :
            answer = _
            break
    return answer

def main() :
    n = int(sys.stdin.readline())
    sys.stdout.write(''.join([str(solution(n)), '\n']))

if __name__ == "__main__" :
    main()