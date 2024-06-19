def solution(x):
    string_sum = 0
    string = str(x)
    
    for i in string:
        string_sum += int(i)
    
    if x % string_sum == 0 :
        return True
    else:
        return False