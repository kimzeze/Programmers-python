def solution(numbers):
    SUM = 0  # SUM을 0으로 초기화
    for i in numbers:
        SUM += i
    AVG = SUM / len(numbers)  
    return AVG  # 계산된 평균을 반환