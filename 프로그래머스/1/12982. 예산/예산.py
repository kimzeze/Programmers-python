def solution(d, budget):
    answer = ''
    d.sort()
    
    result_list = []
    
    for i in d :
        if i <= budget:
            result_list.append(i)
            budget -= i
        else:
            break;
    answer = len(result_list)
    return answer