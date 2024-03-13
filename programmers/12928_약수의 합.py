# 2024-03-13
import sys

def solution(n):
    answer = 0
    for _ in range(1, n+1) :
        if n  % _ == 0 :
            answer += _
    return answer

def main() :
    n = int(sys.stdin.readline())
    sys.stdout.write(''.join([str(solution(n)), '\n']))

if __name__ == "__main__" :
    main()