def solution(my_string):
    answer = ''
    my_list = ['a','e','i','o','u']
    for string in my_string:
        if string not in my_list:
            answer += string
    return answer