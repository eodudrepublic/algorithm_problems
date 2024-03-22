def calculate_max_velocity(a, b, c, d, o, k):
    # 제약 조건을 만족하는 속도의 최댓값 계산
    max_velocity = k / o
    
    # 속도의 최댓값이 100 이하인지 확인
    if max_velocity <= 100:
        return round(max_velocity, 2)
    else:
        # 속도의 최댓값이 100을 초과하면 100으로 설정
        return 100

def main():
    a, b, c, d, o, k = map(float, input().split())
    
    # 최대 속도 계산
    max_velocity = calculate_max_velocity(a, b, c, d, o, k)
    print("속도의 최댓값:", max_velocity, "km/h")

if __name__ == "__main__":
    main()
