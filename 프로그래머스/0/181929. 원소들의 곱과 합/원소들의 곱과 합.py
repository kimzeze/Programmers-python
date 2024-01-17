def solution(num_list):
    answer = 0
    mul = 1
    add = 0
    
    for i in num_list:
        mul *= i
        add += i
        
    
    if mul < add*add :
        return 1
    
    else:
        return 0
    
