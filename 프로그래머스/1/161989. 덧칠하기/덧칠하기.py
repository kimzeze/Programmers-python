def solution(n, m, section):
    answer = 0
    first_section = section[0]
    last_section = section[-1] 
    current = 0
    
    for i in section:
        if current < i:
            current = i - 1 + m
            answer += 1

    return answer
        