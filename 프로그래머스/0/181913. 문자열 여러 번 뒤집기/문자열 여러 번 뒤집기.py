def solution(my_string, queries):
    my_string = list(my_string)
    
    for query in queries:
        s, e = query
        my_string[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_string)

# 무슨 말인지 잘 모르겠다