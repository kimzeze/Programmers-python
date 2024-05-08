def solution(s, skip, index):
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    answer = ''

    # skip 문자열 제거
    for i in skip:
        my_list.remove(i)
        print(my_list)
        
    
    for target in s:
        old_index = my_list.index(target)
        new_index = (old_index + index) % len(my_list)
        answer += my_list[new_index]
        
    return answer