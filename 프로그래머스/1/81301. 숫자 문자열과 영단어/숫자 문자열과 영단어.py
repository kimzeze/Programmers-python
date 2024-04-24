def solution(s):
    answer = ''
    
    my_list = []
    check_string = ''
    number = ['0', '1', '2', '3', '4', '5', '6', '7' ,'8', '9']
    string_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # 앞에서 부터 숫자가 있는지 파악한다
    for target in s:
        # 숫자일 경우
        if target in number:
            my_list.append(target)
        # 문자일 경우
        else:
            check_string += target
            if check_string in string_list:
                my_list.append(str(string_list.index(check_string)))
                
                # 초기화
                check_string = '' 
    
    print(my_list)
    for i in my_list:
        answer += i 
        
    return int(answer)