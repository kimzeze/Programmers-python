def solution(my_string, m, c):
    answer = ''
    index = c - 1
    while index < len(my_string):
        answer += my_string[index]
        index += m
    return answer