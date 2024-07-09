def solution(lottos, win_nums):
    answer = []
    win_arr = [6,6,5,4,3,2,1]
    
    count = 0 
    zero = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        elif lotto == 0 :
            zero += 1
    
    answer.append(win_arr[count + zero])
    answer.append(win_arr[count])
    
    return answer