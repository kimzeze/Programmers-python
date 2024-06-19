def solution(n):
    answer = []
    string_n = str(n)
    
    for i in string_n:
        answer.append(int(i))
    return answer[::-1]