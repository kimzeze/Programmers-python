def solution(my_string, s, e):
    target = my_string[s:e+1]
    reversed_target = target[::-1]
    answer = my_string[:s] + reversed_target + my_string[e+1:]
    return answer