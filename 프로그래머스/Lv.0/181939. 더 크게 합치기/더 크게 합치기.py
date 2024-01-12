def solution(a, b):
    
    case1 = str(a) + str(b)
    case2 = str(b) + str(a)
    
    if case1 > case2:
        answer = int(case1)
    else:
        answer = int(case2)
    
    return answer