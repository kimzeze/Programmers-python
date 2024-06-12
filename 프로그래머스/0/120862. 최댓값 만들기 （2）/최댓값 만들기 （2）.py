def solution(numbers):
    answer = 0
    
    # 리스트를 내림차순으로 정렬
    numbers.sort(reverse=True)
    
    # 양수 두개의 곱과 음수 두개의 곱을 비교해서 큰 수 리턴
    if numbers[0]*numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0]*numbers[1]
    else:
        return numbers[-1]*numbers[-2]
    