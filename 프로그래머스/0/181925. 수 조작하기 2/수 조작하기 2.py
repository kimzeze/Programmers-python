def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        min = numLog[i] - numLog[i-1]
        
        if min == 1:
            answer += 'w'
        elif min == -1:
            answer += 's'
        elif min == 10:
            answer += 'd'
        elif min == -10:
            answer += 'a'
    
    return answer