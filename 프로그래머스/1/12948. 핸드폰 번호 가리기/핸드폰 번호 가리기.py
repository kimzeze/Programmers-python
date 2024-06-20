def solution(phone_number):
    answer = ''
    length = len(phone_number)
    
    for _ in range(length - 4):
        answer += '*'
    
    answer += phone_number[length - 4 : length]
    
    return answer