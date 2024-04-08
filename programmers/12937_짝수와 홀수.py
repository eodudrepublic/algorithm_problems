# 2024-4-08 (04-09)
import sys

def solution(num):
    if num % 2 :
        answer = 'Odd'
    else :
        answer = 'Even'
    return answer

def main() :
    num = int(sys.stdin.readline())
    sys.stdout.write(''.join([str(solution(num)), '\n']))

if __name__ == "__main__" :
    main()