def solution(my_string):
    answer = []
    sort_answer = ''
    for string in my_string:
        answer.append(string.lower())
        
    answer.sort()
    
    for i in answer:
        sort_answer += i
    
    
    return sort_answer