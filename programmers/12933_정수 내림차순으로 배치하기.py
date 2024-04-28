# 2024-04-28 (04-29)
import sys

def solution(n):
    arr = sorted(str(n), reverse=True)
    answer = int(''.join(arr))
    return answer

def main() :
    n = int(sys.stdin.readline())
    sys.stdout.write(''.join([str(solution(n)), '\n']))

if __name__ == "__main__" :
    main()