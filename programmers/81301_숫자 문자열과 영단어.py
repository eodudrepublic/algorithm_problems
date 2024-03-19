# 2024-03-19
import sys

def solution(s):
    arr = []
    L = len(s)
    i = 0
    while i < L :
        if s[i].isdigit() :
            arr.append(s[i])
            i += 1
        elif s[i] == 'z' :
            arr.append('0')
            i += 4
        elif s[i] == 'o' :
            arr.append('1')
            i += 3
        elif s[i] == 't' :
            if s[i+1] == 'w' :
                arr.append('2')
                i += 3
            elif s[i+1] == 'h' :
                arr.append('3')
                i += 5
        elif s[i] == 'f' :
            if s[i+1] == 'o' :
                arr.append('4')
                i += 4
            elif s[i+1] == 'i' :
                arr.append('5')
                i += 4
        elif s[i] == 's' :
            if s[i+1] == 'i' :
                arr.append('6')
                i += 3
            elif s[i+1] == 'e' :
                arr.append('7')
                i += 5
        elif s[i] == 'e' :
            arr.append('8')
            i += 5
        elif s[i] == 'n' :
            arr.append('9')
            i += 4
        else : pass
    answer = int(''.join(arr))
    return answer

def main() :
    s = sys.stdin.readline().strip()
    sys.stdout.write(''.join([str(solution(s)), '\n']))

if __name__ == "__main__" :
    main()