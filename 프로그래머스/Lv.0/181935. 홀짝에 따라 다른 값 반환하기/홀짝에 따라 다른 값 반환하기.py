def solution(n):
    answer = 0
#    홀수 일 때
    if n % 2 == 1: 
        for i in range(1, n + 1):
            if i % 2 == 1:
                answer += i
#    짝수 일 때
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                answer += i**2
    
    return answer