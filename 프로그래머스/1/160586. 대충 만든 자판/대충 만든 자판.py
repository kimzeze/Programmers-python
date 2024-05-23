def solution(keymap, targets):
    answer = []
    my_dict = {}
    
    #
    for i in keymap:
        for index, key in enumerate(i):
            if key not in my_dict or my_dict[key] > index + 1:
                my_dict[key] = index + 1
    
    print(my_dict)
    for i in targets:
        result = 0
        print(i)
        for j in i:
            if j in my_dict:
                result += my_dict[j]
            else:
                result = -1 
                break
        answer.append(result)
    
    return answer