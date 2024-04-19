def solution(order):
    answer = 0
    for target in order:
        answer += 4500
        if 'cafelatte' in target:
            answer += 500

            
    return answer