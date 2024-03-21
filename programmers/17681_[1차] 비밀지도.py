import sys

def solution(N, arr1, arr2):
    arr = [2 ** n for n in range(N-1, -1, -1)]
    answer = []
    for n in range(N) :
        line = []
        for _ in arr :
            if arr1[n] // _ == 0 and arr2[n] // _ == 0 :
                line.append(' ')
            else :
                line.append('#')
                arr1[n] = arr1[n] % _
                arr2[n] = arr2[n] % _
        answer.append(''.join(line))
        
    return answer

def main() :
    sys.stdout.write('n : ')
    n = int(sys.stdin.readline())
    sys.stdout.write('arr1 : ')
    arr1 = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write('arr2 : ')
    arr2 = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(''.join([str(solution(n, arr1, arr2)), '\n']))

if __name__ == "__main__" :
    main()