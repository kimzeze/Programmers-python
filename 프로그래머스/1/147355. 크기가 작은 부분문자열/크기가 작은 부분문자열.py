def solution(t, p):
    answer = 0
    
    count = len(t) - len(p) + 1
    
    # str_list = []    
    
    for i in range(count):
        target = t[0+i:len(p)+i]
        if target <= p:
            answer += 1
    

    return answer