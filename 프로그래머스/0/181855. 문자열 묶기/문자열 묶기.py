def solution(strArr):
    answer = {}
    
    for string in strArr:
        length = len(string)
        if length not in answer:
            answer[length] = 0
        answer[length] += 1
    
    return max(answer.values())