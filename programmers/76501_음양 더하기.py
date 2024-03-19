# 2024-03-19
import sys

def solution(absolutes, signs):
    answer = 0
    L = len(signs)
    for l in range(L) :
        if signs[l] :
            answer += absolutes[l]
        else :
            answer -= absolutes[l]
    return answer

def main() :
    absolutes = list(map(int, sys.stdin.readline().split()))
    arr = sys.stdin.readline().strip().split()
    signs = []
    for _ in arr :
        if _ == 'true' :
            signs.append(True)
        else :
            signs.append(False)
    sys.stdout.write(''.join([str(solution(absolutes, signs)), '\n']))

if __name__ == "__main__" :
    main()