def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        my_list = []
        for i in range(1, num // 2 + 1):
            if num % i == 0 :
                my_list.append(i)
        my_list.append(num)   
        if len(my_list) % 2 == 0 :
            answer += num
        else:
            answer -= num
                
    return answer