def solution(a, b):
    
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    my_list = ['FRI', 'SAT', 'SUN','MON','TUE','WED','THU']
    
    result = 0
    
    for i in range(a-1):
        result += days[i]
    
    answer = my_list[(result + b -1) % 7]
    
    return answer